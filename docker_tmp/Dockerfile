# pull official base image
FROM python:3.8

RUN mkdir /app /var/log/app
# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
#COPY entrypoint.sh .

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
#RUN chmod 777 entrypoint.sh && chmod 777 /app/entrypoint.sh


# copy project
COPY . .

#ENTRYPOINT ["/app/entrypoint.sh"]