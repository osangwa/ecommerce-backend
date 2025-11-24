from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .models import Cart, CartItem
from apps.products.models import Product
from .serializers import (
    CartSerializer, 
    AddToCartSerializer, 
    UpdateCartItemSerializer
)

class CartDetailView(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_cart(request):
    serializer = AddToCartSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    
    product_id = serializer.validated_data['product_id']
    quantity = serializer.validated_data['quantity']
    
    cart, created = Cart.objects.get_or_create(user=request.user)
    product = get_object_or_404(Product, id=product_id, is_available=True)
    
    if product.stock_quantity < quantity:
        return Response(
            {"error": f"Only {product.stock_quantity} items available in stock"}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'quantity': quantity, 'price_at_addition': product.price}
    )
    
    if not created:
        cart_item.quantity += quantity
        cart_item.save()
    
    return Response(CartSerializer(cart).data)

@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def update_cart_item(request, item_id):
    try:
        cart = Cart.objects.get(user=request.user)
        cart_item = CartItem.objects.get(id=item_id, cart=cart)
    except (Cart.DoesNotExist, CartItem.DoesNotExist):
        return Response({"error": "Cart item not found"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = UpdateCartItemSerializer(cart_item, data=request.data)
        serializer.is_valid(raise_exception=True)
        
        if cart_item.product.stock_quantity < serializer.validated_data['quantity']:
            return Response(
                {"error": f"Only {cart_item.product.stock_quantity} items available in stock"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer.save()
        return Response(CartSerializer(cart).data)
    
    elif request.method == 'DELETE':
        cart_item.delete()
        return Response(CartSerializer(cart).data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def clear_cart(request):
    try:
        cart = Cart.objects.get(user=request.user)
        cart.items.all().delete()
        return Response(CartSerializer(cart).data)
    except Cart.DoesNotExist:
        return Response({"error": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)