# pull official base image
FROM python:3.8

RUN mkdir /app
# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# todo: update package
RUN apt-get update && \
    apt-get install -y \
        git \
        python3-dev \
        supervisor \
        nano

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . /app