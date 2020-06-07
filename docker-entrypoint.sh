#!/usr/bin/env bash

if [ ! -z ${DEPLOY_DB} ] && $DEPLOY_DB; then
    echo "Create database and loaddata"
    export DJANGO_SUPERUSER_PASSWORD=djangoadmin;python manage.py createsuperuser --noinput --username admin --email django@teste.com && \
    python manage.py makemigrations && \
    python manage.py migrate && \
    python manage.py loaddata payment_method && \
    python manage.py loaddata store && \
    python manage.py loaddata products && \
    python manage.py runserver 0.0.0.0:8000      
else
    echo "Environment not defined at $DEPLOY_DB or is False";
    echo "Do makemigrations and migrate"
    export DJANGO_SUPERUSER_PASSWORD=djangoadmin;python manage.py createsuperuser --noinput --username admin --email django@teste.com && \
    python manage.py makemigrations && \
    python manage.py migrate && \
    python manage.py runserver 0.0.0.0:8000
fi