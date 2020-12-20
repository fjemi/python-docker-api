# Deploy APIs With Python and Docker

## Table of Contents
*  [Introduction](#introduction)
*  [Technologies](#technologies)
*  [Setup](#setup)
*  [Usage](#usage)

## Introduction

A production-ready API developed using Python and FastAPI. The API runs on an Uvicorn, an ASGI server, and is deployed using Docker.

## Technologies

This project is created with
-  [Python](https://www.python.org/)
-  [FastAPI](https://fastapi.tiangolo.com/)
-  [Uvicorn](https://www.uvicorn.org/)
-  [Docker](https://www.docker.com/)
-  [Docker Compose](https://docs.docker.com/compose/)

## Deployment
Install the repo locally
```
$ git clone https://github.com/fjemi/python-docker-api.git python-docker-api
$ cd python-docker-api
```

### Docker Compose
Run `docker-compose up` from the project's root directory to deploy the application

### Docker
To build the app in a Docker image and run the image in a container, execute the following commands from the project's root directory
```
$ cd python-docker-api/api
# build the image
$ docker build -t app-image .
# run image in a container
$ docker run -d --name app-container -p 80:80 app-image
```

## Usage
- Ping the app at [https://0.0.0.0:80](https://0.0.0.0:80)
- Access OpenAPI docs at [https://0.0.0.0:80/docs](https://0.0.0.0:80/docs)

## API Routing
- Routes are defined in `api/app/routes` and are dynamically loaded
- Routes and function loaded within from a route's `.py` file must share the same name