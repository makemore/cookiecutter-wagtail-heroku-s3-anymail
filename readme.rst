cookiecutter-wagtail-heroku-s3-anymail
==========================

A cookiecutter_ template for Wagtail for instant deployment on heroku & s3 with anymail support.

.. _cookiecutter: https://github.com/audreyr/cookiecutter

Description
-----------

The goal of this cookiecutter is to give you an instant starting point for a wagtail deployment, into a production hosting environment.

- django 1.9
- Wagtail 1.5.2
- Heroku settings file (in addition to self managed server)
- .env for environement variables
- S3 support for static and media files (in seperate directorys) in s3 bucket
- Anymail support
- basic auth user/pass block on heroku deployment

Bare bone usage (sans virtual env, not recommended)
------

requirements before running

- created heroku app name

heroku apps:create {{cookiecutter.project_name}} --region eu

- created s3 bucket name

go to s3 and create a bucket, and setup a new isolated user with access to that bucket

This will give you a unique:

- s3 access key and secret key

- sengrid api key with send mail support

Get sendgrid 