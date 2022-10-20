FROM python:3.8-buster

COPY ./pypostgres .

RUN apt-get update -y
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt