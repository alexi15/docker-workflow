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

### Instructions to run luig
In a terminal window navigate to luigi_docker/ and type in the command

> PYTHONPATH='.' luigi --module dockerTask2 DockerTaskRun --local-scheduler

This will run luigi on the file dockerTask2 witch contains the luigi task DockerTaskRun. More instructions can be found in dockerTask2.py. 

#### Install nextflow
> - curl -fsSL get.nextflow.io | bash

##### Move to $PATH
> - sudo mv nextflow /bin

### Instruction to run nextflow
In a terminal window navigate to next_docker/ and type in the command
> nextflow run helloDocker.nf 
