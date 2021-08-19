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

ENV DB_USER=postgres
ENV DB_NAME=cinetpay
ENV DB_PASSWORD=123456
ENV DB_HOST=13.37.112.221
ENV DB_PORT=5432
ENV DJANGO_SETTINGS=testExcel.settings.py
ENV SECRET_KEY=BDN{:v7RQ=9{/y5573~}xnBK}7vw6pQMS]w[8LU@Zasj9}b@u98kX83v)tR2E!2?
ENV DEBUG=False
ENV DJANGO_HOST=13.37.112.221
ENV DJANGO_PORT=7000
ENV CLIENT_ID=grTE4R1H1QRu1zgHcfKiwtkvySFRBbn5WmVmLxML
ENV CLIENT_SECRET=bvsRTGnqgdKnuqb490oTbaRcPD9voTzTrgMm8Hr6Eoufa58zuegmGEnRrLPy2X4atqARcuNnzjaFoy7TKHHsyE31fRhEpUolLApE5MFeObQ7XECVelBEWAuJt2HWI3lN
ENV ANGULAR_HOST=13.37.112.221
ENV ALLOWED_HOST=*
ENV ANGULAR_PORT=82

# COPY ./requirements.txt .
RUN pip install -r requirements.txt


RUN apk add --no-cache bash

EXPOSE 7000
EXPOSE 5432
EXPOSE 82