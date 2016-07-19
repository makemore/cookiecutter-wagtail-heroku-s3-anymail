from django.conf import settings
from storages.backends.s3boto import S3BotoStorage

#Not going to use this for now, will keep static on main server

class StaticStorage(S3BotoStorage):
    location = settings.STATICFILES_LOCATION
    bucket_name = "{{cookiecutter.s3_bucket_name}}"

class MediaStorage(S3BotoStorage):
    location = settings.MEDIAFILES_LOCATION
    bucket_name = "{{cookiecutter.s3_bucket_name}}"
