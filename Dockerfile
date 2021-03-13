FROM python:3.8.5

RUN apt update && \
    apt upgrade -y

RUN pip install --upgrade pip && \
    pip install pypdf2