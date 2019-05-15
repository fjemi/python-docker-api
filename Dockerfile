FROM ubuntu:latest
MAINTAINER Femi Jemilohun "olufemi.jemilohun@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["api.py"] 
