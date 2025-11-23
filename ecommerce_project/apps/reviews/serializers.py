from rest_framework import serializers
from .models import Review, Wishlist
from apps.products.serializers import ProductListSerializer

class ReviewSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)
    product_name = serializers.CharField(source='product.name', read_only=True)
    
    class Meta:
        model = Review
        fields = (
            'id', 'product', 'product_name', 'user_email', 'rating', 
            'title', 'comment', 'is_verified_purchase', 'is_approved',
            'helpful_count', 'created_at', 'updated_at'
        )
        read_only_fields = ('is_verified_purchase', 'is_approved', 'helpful_count')
    
    def validate(self, attrs):
        user = self.context['request'].user
        product = attrs.get('product')
        
        # Check if user has purchased the product
        if not user.orders.filter(
            items__product=product, 
            status='delivered'
        ).exists():
            attrs['is_verified_purchase'] = False
        else:
            attrs['is_verified_purchase'] = True
        
        return attrs

class CreateReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('product', 'rating', 'title', 'comment')
    
    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5")
        return value

class WishlistSerializer(serializers.ModelSerializer):
    product = ProductListSerializer(read_only=True)
    
    class Meta:
        model = Wishlist
        fields = ('id', 'product', 'created_at')