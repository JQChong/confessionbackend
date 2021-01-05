import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'confessionbackend.settings.deployment')

application = get_wsgi_application()