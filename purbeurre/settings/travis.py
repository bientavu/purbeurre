from purbeurre.settings import *

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
