from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product-list'),
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('search/', views.product_search_view, name='product-search'),
    path('<slug:slug>/', views.ProductDetailView.as_view(), name='product-detail'),
]