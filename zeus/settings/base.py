from datetime import timedelta
from pathlib import Path

import environ

env = environ.Env(DEBUG=(bool, False))

environ.Env.read_env()

MODE = env('MODE', default='development')

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = env('SECRET_KEY', default='SECRET')

DEBUG = MODE == 'development'

ALLOWED_HOSTS = env('ALLOWED_HOSTS', default='*').split(',')

APPEND_SLASH = False

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',

    # third party
    'rest_framework',

    # apps
    'users',
    'todo',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'zeus.urls'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(seconds=env.int('ACCESS_TOKEN_LIFETIME', default=60 * 60 * 24)),
    'REFRESH_TOKEN_LIFETIME': timedelta(seconds=env.int('REFRESH_TOKEN_LIFETIME', default=60 * 60 * 24 * 7)),
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'zeus.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        **env.db(default='psql://zeus:zeus@localhost/zeus'),
    },
}

"""
For testing must using dummy cache
'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
"""

REDIS_URL = env('REDIS_URL', default='redis://localhost:6379')

CACHES = {
    'default':
        {
            'BACKEND': 'django_redis.cache.RedisCache',
            'LOCATION': f'{REDIS_URL}',
            'OPTIONS': {
                'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            },
        }
}

# Cacheops Settings
CACHEOPS_ENABLED = True
CACHEOPS_DEFAULTS = {
    'timeout': 60 * 60 * 1
}
CACHEOPS_REDIS = f"{REDIS_URL}/1"
CACHEOPS = {
    '*.*': {'ops': (), 'timeout': 60 * 60},
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles/'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'

AUTH_USER_MODEL = 'users.User'

# Celery Configs (CELERY namespace)

"""
CELERY_BROKER_URL = f"{BROKER}://{BROKER_USER}:{BROKER_PASSWORD}@{BROKER_HOST}:{BROKER_PORT}/{BROKER_VHOST}"
"""

CELERY_BROKER_URL = env.str('CELERY_BROKER_URL', 'redis://localhost:6379/2')

CELERY_ACCEPT_CONTENT = ['application/json', 'pickle']
CELERY_TASK_SERIALIZER = 'pickle'
CELERY_RESULT_SERIALIZER = 'pickle'
CELERY_TRACK_STARTED = True
CELERY_IGNORE_RESULT = False
CELERY_RESULT_BACKEND = env.str('CELERY_RESULT_BACKEND',
                                'db+postgresql://zeus:zeus@localhost/zeus')

USER_AGENTS_CACHE = 'default'

AUTO_USERNAME = False

SITE_ID = 1
