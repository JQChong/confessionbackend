from confessionbackend.settings.base import *

STATIC_ROOT = 'static'

DEBUG = False

SECRET_KEY = os.getenv('CONFESSION_SECRET_KEY')

ALLOWED_HOSTS += [os.getenv('CONFESSION_DOMAIN')]

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    os.getenv('CONFESSION_FRONT_END_DOMAIN'),
)


FRONT_END_DOMAIN = os.getenv('CONFESSION_FRONT_END_DOMAIN')

DEFAULT_RENDERER_CLASSES += (
    'rest_framework.renderers.JSONRenderer',
)

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = DEFAULT_RENDERER_CLASSES
