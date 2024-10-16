#!/bin/sh

# Activate the virtual environment
. venv/bin/activate

# Run Django management commands
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py runserver 0.0.0.0:8000
