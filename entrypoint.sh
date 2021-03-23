#!/bin/bash

pyton manage.py makemigrations --no-input

python manage.py migrate --no-input

exec gunicorn docker_tmp.wsgi:application -b 0.0.0.0:8000 --reload

sleep 1d
