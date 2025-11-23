from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404

from .models import Review, Wishlist
from apps.products.models import Product
from .serializers import (
    ReviewSerializer,
    CreateReviewSerializer,
    WishlistSerializer
)

class ReviewListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        product_id = self.kwargs.get('product_id')
        if product_id:
            return Review.objects.filter(
                product_id=product_id, 
                is_approved=True
            ).select_related('user', 'product')
        return Review.objects.filter(is_approved=True).select_related('user', 'product')
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateReviewSerializer
        return ReviewSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def mark_review_helpful(request, review_id):
    review = get_object_or_404(Review, id=review_id, is_approved=True)
    review.helpful_count += 1
    review.save()
    return Response({"helpful_count": review.helpful_count})

class WishlistListView(generics.ListCreateAPIView):
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user).select_related('product')
    
    def perform_create(self, serializer):
        product_id = self.request.data.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        
        # Check if already in wishlist
        if Wishlist.objects.filter(user=self.request.user, product=product).exists():
            return Response(
                {"error": "Product already in wishlist"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer.save(user=self.request.user, product=product)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_from_wishlist(request, product_id):
    wishlist_item = get_object_or_404(
        Wishlist, 
        user=request.user, 
        product_id=product_id
    )
    wishlist_item.delete()
    return Response({"message": "Removed from wishlist"})