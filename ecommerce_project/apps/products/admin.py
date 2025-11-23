from django.contrib import admin
from .models import Category, Product, ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'is_active', 'display_order')
    list_filter = ('is_active', 'parent')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock_quantity', 'is_available', 'is_featured')
    list_filter = ('category', 'is_available', 'is_featured', 'created_at')
    search_fields = ('name', 'sku', 'description')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline]
    
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'description', 'short_description', 'category', 'sku')
        }),
        ('Pricing', {
            'fields': ('price', 'compare_at_price', 'cost_price')
        }),
        ('Inventory', {
            'fields': ('stock_quantity', 'low_stock_threshold')
        }),
        ('Properties', {
            'fields': ('weight', 'dimensions')
        }),
        ('Status', {
            'fields': ('is_available', 'is_featured')
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description')
        }),
    )