#To run on luigi without parameters
#PYTHONPATH='.' luigi --module dockerTask2 DockerTaskRun --local-scheduler
#Example of running with parameters
#PYTHONPATH='.' luigi --module dockerTask2 DockerTaskRun --imageName myimage --local-scheduler

'''
Simple example of running luigi tasks in docker containers. 
'''

import os
import luigi
import docker

client = docker.from_env() #create a docker client

#Luigi task to create a docker image. Takes in two parameters for image name and dockerfile.
class DockerImageCreate(luigi.Task):
    imageName = luigi.Parameter(default = "myimage")
    dockerFile = luigi.Parameter(default = "Dockerfile")
    id = 1
    def output(self): #the output is a simple file with the image id. 
        return luigi.LocalTarget("dockerResults/imageID_{}.tsv".format(self.id))        
    def run(self): 
        cwd = os.getcwd()
        
        #client.images.remove('myimage', force=True)
        with open(self.dockerFile) as f:
            img = client.images.build(path='.', fileobj=f, tag=self.imageName) #build a docker image using the dockerfile and imageName
        self.id = img.id
        with self.output().open('w') as out_file:
            out_file.write(str(self.id))

#Luigi task to run a task on the docker image. Requires DockerImageCreate to have executed correctly.
class DockerTaskRun(luigi.Task):
    imageName = luigi.Parameter(default = "myimage")
    id = 1
    def requires(self):
        return [DockerImageCreate()]
    def output(self):
        return luigi.LocalTarget("dockerResults/imageOutput_{}.tsv".format(self.id))
    def run(self):
        
        cnt = client.containers.run(self.imageName, detach=True, volumes={'/home/alex/luigi_docker': {'bind': '/home/luigi_docker', 'mode': 'rw'}})
        self.id = cnt.id
        print("container id {}".format(self.id))
        with self.output().open('w') as out_file:
            for conn in client.containers.list():
                out_file.write("{} \n".format(conn))
    
    
    

    


    
