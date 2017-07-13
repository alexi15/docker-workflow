import os
import docker

def dockerTest():
#    os.system("docker build -tq \"dockerfile\" .")
 #   id = os.system("docker images dockerfile --format \"{{.ID}}\"")
  #  print(id)
    cwd = os.getcwd()
    client = docker.from_env()
    
    #client.images.remove('myimage', force=True)
    with open('Dockerfile') as f:
        client.images.build(path=cwd, fileobj=f, tag='myimage')
    
    cnt = client.containers.run("myimage", detach=True, volumes={'/home/alex/luigi_docker': {'bind': '/home/luigi_docker', 'mode': 'rw'}})
    containe = client.containers.get(cnt.id)

    print(cnt.attrs['Config']['Image'])
    #print(cnt.exec_run('python hello.py'))
    print("continaer id {}".format(cnt.id))
    print(client.containers.list())
    
    #print(client.containers.run("myimage", "ls "))
    
    client.images.remove("myimage", force=True)
    
    print(client.containers.list()) 

if __name__ == "__main__":
    dockerTest()


#dockerfile
