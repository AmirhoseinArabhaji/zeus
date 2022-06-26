import environ

from ..celery import celery_app

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env()
MODE = env('MODE', default='development')

if MODE == 'development':
    from .development import *
elif MODE == 'production':
    from .production import *
elif MODE == 'staging':
    from .staging import *

__all__ = ['celery_app']
