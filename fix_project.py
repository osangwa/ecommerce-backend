#!/usr/bin/env python3
import os

print("🚀 Fixing E-commerce Project Structure...")

# Create essential __init__.py files
init_files = [
    'ecommerce_project/__init__.py',
    'ecommerce_project/config/__init__.py', 
    'ecommerce_project/apps/__init__.py',
    'ecommerce_project/apps/users/__init__.py',
    'ecommerce_project/apps/products/__init__.py',
    'ecommerce_project/apps/cart/__init__.py',
    'ecommerce_project/apps/orders/__init__.py',
    'ecommerce_project/apps/reviews/__init__.py'
]

for file_path in init_files:
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as f:
        pass
    print(f"✅ Created {file_path}")

# Create settings.py
settings_content = '''
import os
from pathlib import Path
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent.parent
SECRET_KEY = 'dev-key-change-in-production'
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'drf_yasg',
    'ecommerce_project.apps.users',
    'ecommerce_project.apps.products',
    'ecommerce_project.apps.cart',
    'ecommerce_project.apps.orders',
    'ecommerce_project.apps.reviews',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ecommerce_project.config.urls'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'users.User'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
}
'''

with open('ecommerce_project/config/settings.py', 'w') as f:
    f.write(settings_content)
print("✅ Created ecommerce_project/config/settings.py")

# Create urls.py
urls_content = '''
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="E-Commerce API",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('api/auth/', include('ecommerce_project.apps.users.urls')),
    path('api/products/', include('ecommerce_project.apps.products.urls')),
    path('api/cart/', include('ecommerce_project.apps.cart.urls')),
    path('api/orders/', include('ecommerce_project.apps.orders.urls')),
    path('api/reviews/', include('ecommerce_project.apps.reviews.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''

with open('ecommerce_project/config/urls.py', 'w') as f:
    f.write(urls_content)
print("✅ Created ecommerce_project/config/urls.py")

print("🎉 Project structure fixed! Now run:")
print("python manage.py migrate")