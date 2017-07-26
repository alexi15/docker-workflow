import subprocess
import sys
import time

def repeat(n):
    start = time.time()
    for i in range(n):
        print("\n".format(i))
        subprocess.call("PYTHONPATH='.' luigi --module luigiRandJoinPresentation luigiJoinRandTask --intRange {} --stringRange {} --local-scheduler".format(i,i), shell=True)
    print('------------------------------\n Time {}'.format(time.time() - start))
if __name__ == '__main__':
    if (len(sys.argv) == 1):
        n = 10
    else:
        n = int(sys.argv[1])
    repeat(n)
