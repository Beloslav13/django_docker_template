# pull official base image
FROM python:3.8

RUN mkdir /app \
          /var/log/app

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update && \
    apt install -y \
    supervisor \
    nano

COPY requirements.txt .

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Для запуска gunicorn celery celery_beat через супервизор
#COPY config/supervisor.conf /etc/supervisor/conf.d/docker_tmp.conf

# copy project
COPY . .
