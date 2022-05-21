FROM python:3-alpine

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt


RUN python -m pip install gunicorn

RUN npm install npm@latest -g
RUN npm install -g @angular/cli
COPY .. /code/

EXPOSE 8000

