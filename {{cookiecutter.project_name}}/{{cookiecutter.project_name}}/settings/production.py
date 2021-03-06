from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '{{cookiecutter.project_name}}',
        'USER': '{{cookiecutter.project_name}}',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

try:
    from .local import *
except ImportError:
    pass
