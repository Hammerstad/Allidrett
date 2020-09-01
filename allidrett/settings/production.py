from allidrett.settings.base import *
import os

DEBUG = False
SECRET_KEY = os.environ['SECRET_KEY']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['POSTGRES_USERNAME'],
        'USER': os.environ['POSTGRES_USERNAME'],
        'PASSWORD': os.environ['POSTGRES_PASSWORD'],
        'HOST': os.environ['POSTGRES_HOST'],
        'PORT': '5432',
    }
}
