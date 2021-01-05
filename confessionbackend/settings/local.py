from confessionbackend.settings.base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'on#(sz1xlt-99-zj8y5wwi+l$u^p8y^p-1ef-5m_0@6787s2nn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    'http://localhost:4200',
    'http://127.0.0.1:4200'
)

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}