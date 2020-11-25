#!/bin/sh

set -e


python manage.py collectstatic --noinput
python manage.py migrate
# python manage.py createsuperuser --noinput

uwsgi --socket :8000 --master --enable-threads --module employeeSystem.wsgi
