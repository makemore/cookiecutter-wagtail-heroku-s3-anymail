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

I think this command binds a folder to an app, so you might find it easier to create the app in the web interface.

heroku apps:create {{cookiecutter.project_name}} --region eu

or after creating the app remotely

heroku git:remote -a demo-cookie

- created s3 bucket name

go to s3 and create a bucket, and setup a new isolated user with access to that bucket

This will give you a unique:

- s3 access key and secret key

- sengrid api key with send mail support

Get sendgrid


run cookiecutter in your projects folder

add info as requested

- init git
- push to github
- heroku git:remote -a demo-cookie
- heroku plugins:install git://github.com/ddollar/heroku-config.git
- heroku config:push
- git push heroku master
- heroku run python manage.py migrate
- heroku run python manage.py createsuperuser
- heroku ps:scale web=1
- heroku plugins:install git://github.com/ddollar/heroku-config.git
- heroku config:push

- heroku buildpacks:add --index 1 heroku/nodejs


TODO
-----

-Currently, as we are using the standard python buildpack, as well as the normal node js one, this means that collect static runs twice.
-Once at the end of the normal compile step, which means it hasn't seen the output of manage.py compress
-And again, after the compress step.

This is obviously ineffecient.

- Potentially the best thing to do would be to add install node js steps into the bin folder, as well as bower
- Also would have to create a varient of the python heroku buildpack, that runs compress before collectstatic


S3 help
--------


bucket policy

THE USERS ARN IS LONG KEY LIKE STRING WHICH IDENTIFIES THEM.

{
	"Version": "2008-10-17",
	"Statement": [
		{
			"Sid": "PublicReadForGetBucketObjects",
			"Effect": "Allow",
			"Principal": {
				"AWS": "*"
			},
			"Action": "s3:GetObject",
			"Resource": "arn:aws:s3:::demo-cookie/*"
		},
		{
			"Sid": "",
			"Effect": "Allow",
			"Principal": {
				"AWS": "{{ PUT THE USERS ARN HERE }}"
			},
			"Action": "s3:*",
			"Resource": [
				"arn:aws:s3:::demo-cookie/*",
				"arn:aws:s3:::demo-cookie"
			]
		}
	]
}


Change allowed header to *, but restrict origin to what you want when in production


<CORSConfiguration>
    <CORSRule>
        <AllowedOrigin>*</AllowedOrigin>
        <AllowedMethod>GET</AllowedMethod>
        <MaxAgeSeconds>3000</MaxAgeSeconds>
        <AllowedHeader>*</AllowedHeader>
    </CORSRule>
</CORSConfiguration>
