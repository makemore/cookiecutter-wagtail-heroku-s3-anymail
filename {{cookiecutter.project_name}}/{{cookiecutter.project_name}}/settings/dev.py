from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9ds-2n4(cst28+q316p^$qmulww@r-si!$&%*m$2yaoe&tjs+='


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '{{cookiecutter.project_name}}',
        'USER': 'chris',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

ENABLE_DEV_S3 = True

if ENABLE_DEV_S3:
    INSTALLED_APPS.insert(0, 'collectfast')

    AWS_STORAGE_BUCKET_NAME = 'lolc'
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    STATIC_ROOT = 'static'
    STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATIC_ROOT)

    MEDIA_ROOT = 'media'
    MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIA_ROOT)

    AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

    # AWS_HEADERS = {  # see http://developer.yahoo.com/performance/rules.html#expires
    #    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    #    'Cache-Control': 'max-age=94608000',
    # }

    STATICFILES_LOCATION = "static"
    MEDIAFILES_LOCATION = "media"

    STATICFILES_STORAGE = 'lolc.custom_storages.StaticStorage'
    DEFAULT_FILE_STORAGE = 'lolc.custom_storages.MediaStorage'


    AWS_PRELOAD_METADATA = True

    COMPRESS_STORAGE = STATICFILES_STORAGE
    COMPRESS_URL = STATIC_URL
    COMPRESS_ROOT = STATIC_ROOT

    COMPRESS_OFFLINE = True


try:
    from .local import *
except ImportError:
    pass
