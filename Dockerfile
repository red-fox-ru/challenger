FROM python:3.9.5
LABEL Author="PaninStanislav"

WORKDIR /usr/src/app

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000