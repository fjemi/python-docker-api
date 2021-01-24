# build stage
FROM python:3.8.3-slim-buster as build

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install python dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
COPY Pipfile* /tmp/
RUN cd /tmp && pipenv lock --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt
COPY ./app /app

# production stage
# expose image port
EXPOSE 80
# set enviroment variable
ENV PYTHONPATH="/app/routes/"
# spin up web server
CMD ["sh", "-c", "python app/app.py"]
