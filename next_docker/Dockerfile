#
# Super simple example of a Dockerfile
#
FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y python python-pip wget
RUN pip install Flask

add . /home


WORKDIR /home

CMD ["python", "hello.py"]
