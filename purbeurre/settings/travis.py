from purbeurre.settings import *
import os
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'purbeurre.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
