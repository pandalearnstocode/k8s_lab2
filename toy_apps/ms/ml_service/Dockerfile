FROM python:3.8
COPY ./shopping /usr/src/shopping
COPY ./requirements-api.txt /usr/src/
RUN pip3 install --upgrade pip
RUN pip3 install -r /usr/src/requirements-api.txt
WORKDIR /usr/src
CMD gunicorn --bind 0.0.0.0:5000 shopping.main:app -w 4 -k uvicorn.workers.UvicornWorker --access-logfile - --error-logfile - --log-level info

# # pull official base image
# FROM python:3.9-slim-buster

# # set working directory
# WORKDIR /usr/src/app

# # set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# # install system dependencies
# RUN apt-get update \
#   && apt-get -y install netcat gcc postgresql \
#   && apt-get clean

# # install python dependencies
# RUN pip install --upgrade pip
# COPY ./requirements.txt .
# RUN pip install -r requirements.txt

# # add app
# COPY . .