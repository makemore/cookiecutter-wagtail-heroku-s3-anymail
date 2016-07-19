from __future__ import absolute_import, unicode_literals
import dj_database_url
from .base import *
import os

DEBUG = False

env = os.environ.copy()
SECRET_KEY = env['SECRET_KEY']


DATABASES = {
    'default': dj_database_url.config()
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

INSTALLED_APPS.insert(0, 'collectfast')

AWS_STORAGE_BUCKET_NAME = '{{cookiecutter.s3_bucket_name}}'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
STATIC_ROOT = 'static'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATIC_ROOT)

MEDIA_ROOT = 'media'
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIA_ROOT)


AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

#AWS_HEADERS = {  # see http://developer.yahoo.com/performance/rules.html#expires
#    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
#    'Cache-Control': 'max-age=94608000',
#}

STATICFILES_LOCATION = "static"
MEDIAFILES_LOCATION = "media"

STATICFILES_STORAGE = '{{cookiecutter.project_name}}.custom_storages.StaticStorage'
DEFAULT_FILE_STORAGE = '{{cookiecutter.project_name}}.custom_storages.MediaStorage'

AWS_PRELOAD_METADATA = True

BASIC_WWW_AUTHENTICATION_USERNAME = "{{cookiecutter.project_name}}"
BASIC_WWW_AUTHENTICATION_PASSWORD = "{{cookiecutter.project_name}}123"
BASIC_WWW_AUTHENTICATION = True

try:
    from .local import *
except ImportError:
    pass
