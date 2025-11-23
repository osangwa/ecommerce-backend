from django.urls import path
from . import views

urlpatterns = [
    path('reviews/', views.ReviewListView.as_view(), name='review-list'),
    path('reviews/product/<int:product_id>/', views.ReviewListView.as_view(), name='product-reviews'),
    path('reviews/<int:pk>/', views.ReviewDetailView.as_view(), name='review-detail'),
    path('reviews/<int:review_id>/helpful/', views.mark_review_helpful, name='mark-review-helpful'),
    path('wishlist/', views.WishlistListView.as_view(), name='wishlist'),
    path('wishlist/<int:product_id>/', views.remove_from_wishlist, name='remove-from-wishlist'),
]