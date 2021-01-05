from confessionbackend.settings.base import *

STATIC_ROOT = 'static'

DEBUG = False

SECRET_KEY = os.getenv('CONFESSION_SECRET_KEY')

ALLOWED_HOSTS += [os.getenv('CONFESSION_DOMAIN')]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nusmuvpr_confessiondb'
        'USER': 'nusmuvpr_superuser'
        'PASSWORD': 'msl2020NUS!'
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    os.getenv('CONFESSION_FRONT_END_DOMAIN')
)


FRONT_END_DOMAIN = os.getenv('CONFESSION_FRONT_END_DOMAIN')

# run pip insall mysqlclient in the virtual environment while setting up

pymysql.version_info = (1, 4, 2, "final", 0)
pymysql.install_as_MySQLdb()