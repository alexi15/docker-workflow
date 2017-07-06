# Docker-workflow
Simple examples on how to use docker with workflow managers like Luigi and Nextflow. 

### Setup

#### Setup Python
> - sudo apt-get install python
> - pip install -U pip setuptools

#### Install Docker
> - sudo apt-get install docker
> - pip install docker_py

#### Install luigi
> - pip install luigi

### Instructions to run
In a terminal window type in the command

> PYTHONPATH='.' luigi --module dockerTask2 DockerTaskRun --local-scheduler

This will run luigi on the file dockerTask2 witch contains the luigi task DockerTaskRun. More instructions can be found in dockerTask2.py. 
