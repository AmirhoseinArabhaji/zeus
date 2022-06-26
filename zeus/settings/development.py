from .base import *

ALLOWED_HOSTS = ['*']

INTERNAL_IPS = [
    '127.0.0.1',
    'localhost',
]

INSTALLED_APPS += [
    'debug_toolbar',
    'django_extensions',
]

APPEND_SLASH = True

MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware',
              'django.middleware.locale.LocaleMiddleware'] + MIDDLEWARE

HOST = env.str(var='HOST', default='127.0.0.1:8000')
SITE_URL = f'http://{HOST}/'

CACHEOPS_ENABLED = env.bool('CACHEOPS_ENABLED', default=False)
