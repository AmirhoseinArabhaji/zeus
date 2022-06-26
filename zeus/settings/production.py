from .base import *

ALLOWED_HOSTS = [

]

DEBUG = False

APPEND_SLASH = True

CACHEOPS_ENABLED = env.bool('CACHEOPS_ENABLED', default=True)
AUTO_USERNAME = env.bool('AUTO_USERNAME', default=False)

HOST = env.str(var='HOST', default='site_url')
SITE_URL = f'https://{HOST}/'
