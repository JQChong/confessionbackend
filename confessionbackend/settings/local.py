from confessionbackend.settings.base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'on#(sz1xlt-99-zj8y5wwi+l$u^p8y^p-1ef-5m_0@6787s2nn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

STATIC_URL = '/static'
STATIC_ROOT = 'static'

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    'http://localhost:4200',
    'http://127.0.0.1:4200'
)

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
    # 'default': {
        # 'ENGINE': 'django.db.backends.postgresql',
        # 'HOST': '/cloudsql/white-cedar-305506:asia-southeast1:confessiondb',
        # 'USER': 'postgres',
        # 'PASSWORD': 'sooperuser',
        # 'NAME': 'confessiondb'
    # }
# }

if os.getenv('GAE_APPLICATION', None):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'HOST': '/cloudsql/white-cedar-305506:asia-southeast1:confessiondb',
            'USER': 'postgres',
            'PASSWORD': 'sooperuser',
            'NAME': 'confessiondb'
        }
    }
else:
    # to start, insert cloud_sql_proxy -instances="white-cedar-305506:asia-southeast1:confessiondb"=tcp:3306
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'HOST': '127.0.0.1',
            'PORT': '3306',
            'NAME': 'confessiondb',
            'USER': 'postgres',
            'PASSWORD': 'sooperuser',
        }
    }
# end db_setup