from .base_settings import *

# DEBUG
# ------------------------------------------------------------------------------
DEBUG = True

# Mail settings
# ------------------------------------------------------------------------------

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_PORT = 1025

EMAIL_HOST = 'localhost'


# CACHING
# ------------------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/2.0/ref/settings/#databases
# Uses django-environ to accept uri format
# See: https://django-environ.readthedocs.io/en/latest/#supported-types
# 
# To use SQLite, use the following parameters:
# 'ENGINE': 'django.db.backends.sqlite3',
# 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
DATABASES = {
    'default': {
	'ENGINE': 'django.db.backends.postgresql',
	'NAME': 'unlabel',
	'USER': 'amechiegbe',
	'PASSWORD': '',
	'HOST': 'localhost',
	'PORT': 5432
    }
}
DATABASES['default']['ATOMIC_REQUESTS'] = True


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'http')

