from .base import *

ALLOWED_HOSTS = [

]

DEBUG = True

APPEND_SLASH = True

CACHEOPS_ENABLED = env.bool('CACHEOPS_ENABLED', default=True)
AUTO_USERNAME = env.bool('AUTO_USERNAME', default=False)

HOST = env.str(var='HOST', default='test_server_url')
SITE_URL = f'https://{HOST}/'
