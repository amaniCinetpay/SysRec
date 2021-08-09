# # pull official base image
# FROM python:3.9-slim-buster

# pull official base image
FROM python:3.9-alpine



# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache musl-dev libffi-dev openssl-dev

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
# RUN pip3 install --upgrade pip setuptools wheel
# RUN pip3 install django-oauth-toolkit
# copy project
# COPY . .
ADD . /app/


# set work directory
WORKDIR /app

VOLUME /app/logs

#RUN pip3 install -r /app/api_test/requirements.txt



# COPY ./requirements.txt .
RUN pip install -r requirements.txt

RUN apk add --no-cache bash

EXPOSE 7000
EXPOSE 5432
EXPOSE 82