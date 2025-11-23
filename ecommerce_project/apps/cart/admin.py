from django.contrib import admin
from .models import Cart, CartItem

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'session_key', 'total_items', 'subtotal', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__email', 'session_key')
    inlines = [CartItemInline]
    
    def total_items(self, obj):
        return obj.total_items
    total_items.short_description = 'Total Items'
    
    def subtotal(self, obj):
        return f"${obj.subtotal:.2f}"
    subtotal.short_description = 'Subtotal'

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity', 'price_at_addition', 'total_price')
    list_filter = ('created_at',)
    search_fields = ('cart__user__email', 'product__name')
    
    def total_price(self, obj):
        return f"${obj.total_price:.2f}"
    total_price.short_description = 'Total Price'