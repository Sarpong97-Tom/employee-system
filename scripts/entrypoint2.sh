#!/bin/sh

set -e


python manage.py migrate
python manage.py syncdb --noinput
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin@amin.com', 'keypass')" | python manage.py shell
python manage.py runserver