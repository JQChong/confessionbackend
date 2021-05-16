from confessionbackend.settings.base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'on#(sz1xlt-99-zj8y5wwi+l$u^p8y^p-1ef-5m_0@6787s2nn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

STATIC_ROOT = 'static'

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    'http://localhost:4200',
    'http://127.0.0.1:4200'
)

DEFAULT_RENDERER_CLASSES += (
    'rest_framework.renderers.JSONRenderer',
    'rest_framework.renderers.BrowsableAPIRenderer',
)

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = DEFAULT_RENDERER_CLASSES