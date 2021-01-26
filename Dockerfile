# build
FROM python:3.8.3-alpine as build

# set enviroment variable
ENV PYTHONPATH="/app/routes/"

WORKDIR /
COPY ./app/ ./app

WORKDIR /app
# upgrde pip and install pipenv
RUN ["sh", "-c", "/usr/local/bin/python -m pip install --upgrade pip"]
RUN ["sh", "-c", "pip install pipenv"]
# install dependancies
RUN ["sh", "-c", "pipenv lock"]
RUN ["sh", "-c", "pipenv install --system"]

# production
# expose image port
EXPOSE 80
# run server
CMD ["sh", "-c", "pipenv run python app.py"]
#CMD ["sh", "-c", "ls app -a;"]