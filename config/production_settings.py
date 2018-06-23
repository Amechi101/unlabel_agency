import dj_database_url

from .base_settings import *

DEBUG = False

STATIC_ROOT = os.path.join(BASE_DIR, 'unlabel', 'static')

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SECURE_SSL_REDIRECT = True

SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_BROWSER_XSS_FILTER = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

CSRF_COOKIE_HTTPONLY = True

X_FRAME_OPTIONS = 'DENY'

DATABASES = {
   'default': dj_database_url.config(default='postgres://jgdavlmmmlhymo:c257c5c9e7e944e994844c0e751cc02d9783f92c03a8cd34e557d40e6ad5875b@ec2-54-83-0-158.compute-1.amazonaws.com:5432/d5hjg8s9358vsu')
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'TIMEOUT': 60
    }
}


