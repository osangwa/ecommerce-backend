from .base import *

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']

# Additional development apps
INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# Django Debug Toolbar
INTERNAL_IPS = [
    '127.0.0.1',
]

# Show emails in console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Allow all origins in development
CORS_ALLOW_ALL_ORIGINS = True