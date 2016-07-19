git init
git add .
git commit -m "first commit to heroku"



# Creates a new Heroku app and connects it to your initialised git repo

git push heroku master

# Pushes your commited code up to your new ap

heroku run python manage.py migrate

# Heroku allows you to run shell commands remotely with the 'heroku run' command.

heroku run python manage.py createsuperuser

# Creates a new superuser on Heroku

heroku ps:scale web=1

# Ensures that a new Dyno is running for your project



heroku plugins:install git://github.com/ddollar/heroku-config.git
heroku config:push