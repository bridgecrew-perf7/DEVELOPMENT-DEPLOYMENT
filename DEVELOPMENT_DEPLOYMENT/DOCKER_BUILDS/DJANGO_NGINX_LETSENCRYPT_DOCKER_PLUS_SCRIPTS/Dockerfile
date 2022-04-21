FROM python:3.8-buster

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# copy code files
WORKDIR /usr/src/app

# install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# create directory for the app user
RUN mkdir -p /home/app/_static
WORKDIR /home/app

# copy project
COPY . /home/app
