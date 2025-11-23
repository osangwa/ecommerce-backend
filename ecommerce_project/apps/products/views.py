from rest_framework import generics, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q

from .models import Category, Product
from .serializers import (
    CategorySerializer,
    ProductListSerializer, 
    ProductDetailSerializer, 
    ProductCreateSerializer
)

class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.filter(parent__isnull=True, is_active=True).prefetch_related('children')
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_active']
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CategorySerializer
        return CategorySerializer
    
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminUser()]
        return super().get_permissions()

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    
    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAdminUser()]
        return super().get_permissions()

class ProductListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'is_available', 'is_featured']
    search_fields = ['name', 'description', 'short_description', 'sku']
    ordering_fields = ['price', 'name', 'created_at', 'average_rating', 'sold_count']
    ordering = ['-created_at']
    
    def get_queryset(self):
        queryset = Product.objects.select_related('category').prefetch_related('images')
        
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        
        category_slug = self.request.query_params.get('category')
        if category_slug:
            try:
                category = Category.objects.get(slug=category_slug)
                all_categories = [category] + category.get_all_children()
                queryset = queryset.filter(category__in=all_categories)
            except Category.DoesNotExist:
                pass
        
        in_stock = self.request.query_params.get('in_stock')
        if in_stock and in_stock.lower() == 'true':
            queryset = queryset.filter(stock_quantity__gt=0)
        
        return queryset
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProductCreateSerializer
        return ProductListSerializer
    
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminUser()]
        return super().get_permissions()

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.select_related('category').prefetch_related('images')
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductDetailSerializer
        return ProductCreateSerializer
    
    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAdminUser()]
        return super().get_permissions()
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.view_count += 1
        instance.save(update_fields=['view_count'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

@api_view(['GET'])
def product_search_view(request):
    query = request.query_params.get('search', '')
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | 
            Q(description__icontains=query) |
            Q(short_description__icontains=query) |
            Q(sku__icontains=query)
        ).select_related('category').prefetch_related('images')
        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data)
    return Response([])