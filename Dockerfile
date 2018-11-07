FROM python:3.7.1

RUN apt update -qq \
  && apt install -y build-essential mysql-client --no-install-recommends \
  && rm -rf /var/lib/apt/lists/*

RUN pip install pipenv

WORKDIR /app
