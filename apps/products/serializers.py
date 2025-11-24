from rest_framework import serializers
from .models import Category, Product, ProductImage

class CategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()
    product_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'description', 'image', 'parent', 
                 'children', 'product_count', 'is_active', 'display_order', 
                 'created_at')
    
    def get_children(self, obj):
        children = obj.children.filter(is_active=True)
        return CategorySerializer(children, many=True).data
    
    def get_product_count(self, obj):
        return obj.products.filter(is_available=True).count()

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('id', 'image', 'alt_text', 'is_primary', 'display_order')

class ProductListSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    primary_image = serializers.SerializerMethodField()
    discount_percentage = serializers.ReadOnlyField()
    is_in_stock = serializers.ReadOnlyField()
    is_low_stock = serializers.ReadOnlyField()
    
    class Meta:
        model = Product
        fields = (
            'id', 'name', 'slug', 'short_description', 'price', 
            'compare_at_price', 'discount_percentage', 'stock_quantity',
            'category', 'category_name', 'primary_image', 'is_available',
            'is_featured', 'average_rating', 'review_count', 'is_in_stock',
            'is_low_stock', 'created_at'
        )
    
    def get_primary_image(self, obj):
        primary_image = obj.images.filter(is_primary=True).first()
        if primary_image:
            return ProductImageSerializer(primary_image).data
        return None

class ProductDetailSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    discount_percentage = serializers.ReadOnlyField()
    is_in_stock = serializers.ReadOnlyField()
    is_low_stock = serializers.ReadOnlyField()
    
    class Meta:
        model = Product
        fields = (
            'id', 'name', 'slug', 'description', 'short_description', 
            'price', 'compare_at_price', 'discount_percentage', 'cost_price',
            'stock_quantity', 'low_stock_threshold', 'weight', 'dimensions',
            'category', 'category_name', 'sku', 'images', 'is_available',
            'is_featured', 'average_rating', 'review_count', 'view_count',
            'sold_count', 'is_in_stock', 'is_low_stock', 'meta_title',
            'meta_description', 'created_at', 'updated_at'
        )

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'name', 'description', 'short_description', 'category', 'sku',
            'price', 'compare_at_price', 'cost_price', 'stock_quantity',
            'low_stock_threshold', 'weight', 'dimensions', 'is_available',
            'is_featured', 'meta_title', 'meta_description'
        )