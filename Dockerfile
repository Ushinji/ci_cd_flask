FROM python:3.7.1 AS base
ENV LANG C.UTF-8
ENV APP_ROOT=/app

RUN apt update -qq \
  && apt install -y build-essential mysql-client --no-install-recommends \
  && rm -rf /var/lib/apt/lists/*

RUN pip install pipenv

RUN mkdir $APP_ROOT
WORKDIR $APP_ROOT

ADD Pipfile $APP_ROOT
ADD Pipfile.lock $APP_ROOT
RUN pipenv install --dev --system

COPY . $APP_ROOT

EXPOSE 5000
