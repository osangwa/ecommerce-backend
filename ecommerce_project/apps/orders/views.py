from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.db import transaction

from .models import Order, OrderItem, OrderStatusHistory
from apps.cart.models import Cart, CartItem
from apps.users.models import Address
from .serializers import (
    OrderListSerializer,
    OrderDetailSerializer,
    CreateOrderSerializer
)

class OrderListView(generics.ListAPIView):
    serializer_class = OrderListSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).prefetch_related('items')

class OrderDetailView(generics.RetrieveAPIView):
    serializer_class = OrderDetailSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).prefetch_related(
            'items', 'status_history'
        )

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@transaction.atomic
def create_order(request):
    serializer = CreateOrderSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    
    # Get user's cart
    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        return Response({"error": "Cart is empty"}, status=status.HTTP_400_BAD_REQUEST)
    
    if cart.items.count() == 0:
        return Response({"error": "Cart is empty"}, status=status.HTTP_400_BAD_REQUEST)
    
    # Validate addresses
    shipping_address = get_object_or_404(
        Address, 
        id=serializer.validated_data['shipping_address_id'], 
        user=request.user
    )
    billing_address = get_object_or_404(
        Address, 
        id=serializer.validated_data['billing_address_id'], 
        user=request.user
    )
    
    # Calculate totals
    subtotal = cart.subtotal
    tax_amount = subtotal * 0.18  # 18% tax
    shipping_cost = 10.00  # Fixed shipping cost
    total_amount = subtotal + tax_amount + shipping_cost
    
    # Create order
    order = Order.objects.create(
        user=request.user,
        shipping_address=shipping_address,
        billing_address=billing_address,
        payment_method=serializer.validated_data['payment_method'],
        subtotal=subtotal,
        tax_amount=tax_amount,
        shipping_cost=shipping_cost,
        total_amount=total_amount,
        notes=serializer.validated_data.get('notes', '')
    )
    
    # Create order items
    for cart_item in cart.items.all():
        OrderItem.objects.create(
            order=order,
            product=cart_item.product,
            product_name=cart_item.product.name,
            product_sku=cart_item.product.sku,
            quantity=cart_item.quantity,
            unit_price=cart_item.price_at_addition,
            subtotal=cart_item.total_price
        )
        
        # Update product stock
        cart_item.product.stock_quantity -= cart_item.quantity
        cart_item.product.sold_count += cart_item.quantity
        cart_item.product.save()
    
    # Clear cart
    cart.items.all().delete()
    
    # Create initial status history
    OrderStatusHistory.objects.create(
        order=order,
        status='pending',
        created_by=request.user
    )
    
    return Response(OrderDetailSerializer(order).data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def cancel_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    
    if not order.can_cancel:
        return Response(
            {"error": "Order cannot be cancelled at this stage"}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    order.status = 'cancelled'
    order.cancelled_at = timezone.now()
    order.save()
    
    # Restore product stock
    for order_item in order.items.all():
        product = order_item.product
        product.stock_quantity += order_item.quantity
        product.sold_count -= order_item.quantity
        product.save()
    
    # Update status history
    OrderStatusHistory.objects.create(
        order=order,
        status='cancelled',
        notes=request.data.get('reason', ''),
        created_by=request.user
    )
    
    return Response(OrderDetailSerializer(order).data)