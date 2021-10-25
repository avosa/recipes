# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster

RUN apt-get update && \
    apt-get upgrade -yqq && \
    apt install libpq-dev python3-dev -yqq && \
    apt-get install python3-pip -yqq && \
    pip3 install --upgrade pip && \
    pip3 install psycopg2

WORKDIR /usr/src/app/

COPY requirements.txt /usr/src/app/

ENV REQUIREMENTS_PATH /dependancies

RUN pip3 install -r requirements.txt

COPY .env /usr/src/app/

COPY . /usr/src/app/

ENV export SECRET_KEY=hahah 
ENV export FLASK_CONFIG=production
ENV export FLASK_APP=manage.py
ENV export DATABASE_URL=postgresql://localhost/recipes


EXPOSE 5000

CMD [ "python3", "manage.py", "runserver", "--host=0.0.0.0", "-p", "5000"]
