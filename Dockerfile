FROM python:3.9.4-slim-buster
MAINTAINER rob@circleci.com

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["gunicorn", "src.hello_app:APP"]
