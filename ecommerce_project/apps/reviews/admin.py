from django.contrib import admin
from .models import Review, Wishlist

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'is_verified_purchase', 'is_approved', 'created_at')
    list_filter = ('rating', 'is_verified_purchase', 'is_approved', 'created_at')
    search_fields = ('product__name', 'user__email', 'title', 'comment')
    list_editable = ('is_approved',)
    
    fieldsets = (
        (None, {
            'fields': ('product', 'user', 'order', 'rating')
        }),
        ('Review Content', {
            'fields': ('title', 'comment')
        }),
        ('Status', {
            'fields': ('is_verified_purchase', 'is_approved', 'helpful_count')
        }),
    )

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__email', 'product__name')