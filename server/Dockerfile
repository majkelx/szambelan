FROM python:alpine
MAINTAINER Mikolaj Kaluszynski
LABEL version="0.1"


RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install -r requirements.txt
COPY . /usr/src/app


EXPOSE  8080
ENTRYPOINT ["python3", "./app/server.py"]

