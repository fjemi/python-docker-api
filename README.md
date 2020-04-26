# Docker Python API
A FastAPI application that uses a uvicorn server, deployed in a Docker container

## Usage
1. Clone the repo 
```git clone https://github.com/fjemi/python-docker-api.git python-docker-api```
2. Navigate to the root direcotry of the repo 
```cd python-docker-api```
3. Build a Docker image
```docker build -t api-image .```
4. Run the image in a Docker container
```docker run -d --name api-container -p 80:80 api-image
```
5. Navigate to the url 
  - ```0.0.0.0``` to ping the FastAPI
  - ```0.0.0.0\docs``` to access the OpenAPI documention
