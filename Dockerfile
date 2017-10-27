FROM python:3.6

COPY requirements-dev.txt /requirements-dev.txt
RUN pip3 install -r requirements-dev.txt

WORKDIR /code
