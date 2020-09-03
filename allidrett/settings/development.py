from allidrett.settings.base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'lt*iuhi&z9a$is0*ojma0n!kg6sj4p@!!nklg#d^c_p@!u*+4h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_HOST_USER = "os.environ['EMAIL_ADDRESS']"
# EMAIL_HOST_PASSWORD = os.environ['EMAIL_PASSWORD']
