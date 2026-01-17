FROM python:3.10-alpine
LABEL maintainer="galkaadam4@gmail.com"
WORKDIR /library
ENV PYTHONDONTWRITEBYCODE=1
ENV PYTHONUNBUFFERED=1
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
