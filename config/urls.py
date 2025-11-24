from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse  # Keep this import
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Clean JSON API root - perfect for frontend consumption
def api_root(request):
    return JsonResponse({
        'message': 'E-Commerce API is running! 🚀',
        'version': '1.0',
        'status': 'active',
        'endpoints': {
            'documentation': '/api/docs/',
            'authentication': '/api/auth/',
            'products': '/api/products/',
            'cart': '/api/cart/',
            'orders': '/api/orders/',
            'reviews': '/api/reviews/',
            'admin': '/admin/',
        },
        'documentation': 'Visit /api/docs/ for full API documentation'
    })

schema_view = get_schema_view(
    openapi.Info(
        title="E-Commerce API",
        default_version='v1',
        description="Complete e-commerce backend API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@ecommerce.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Clean JSON API root
    path('', api_root, name='api-root'),
    
    # Admin
    path('admin/', admin.site.urls),
    
    # API Documentation
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    # API Routes
    path('api/auth/', include('apps.users.urls')),
    path('api/products/', include('apps.products.urls')),
    path('api/cart/', include('apps.cart.urls')),
    path('api/orders/', include('apps.orders.urls')),
    path('api/reviews/', include('apps.reviews.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)