FROM python:3.7-slim

ARG DJANGO_PROJECT_NAME
RUN apt-get update && \
    apt-get install -y iputils-ping curl telnet wget traceroute 

COPY requirements.txt /
RUN pip install -U pip && pip install -r requirements.txt
COPY manage.py /app/
COPY ./${DJANGO_PROJECT_NAME} /app/${DJANGO_PROJECT_NAME}
COPY docker-entrypoint.sh /app/

EXPOSE 8000

WORKDIR /app
CMD python3 manage.py runserver 0.0.0.0:8000
