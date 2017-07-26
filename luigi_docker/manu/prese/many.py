import subprocess
import sys
import time

def many(n):
    subprocess.call("rm -r res", shell=True)
    start = time.time()
    #for i in range(n):
        #print("\n".format(i))
    subprocess.call("PYTHONPATH='.' luigi --module luigiRandJoinPresentation luigiJoinRandTask --numberOfRands {} --local-scheduler".format(n), shell=True)

if __name__ == '__main__':
    if (len(sys.argv) == 1):
        n = 10
    else:
        n = int(sys.argv[1])
    many(n)
