#
# Super simple example of a Dockerfile
#
FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y python python-pip wget
RUN pip install Flask

#ADD hello.py /home/hello.py


WORKDIR /home/luigi_docker

CMD ["python", "hello.py"]
