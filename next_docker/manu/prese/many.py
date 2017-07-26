import subprocess
import sys
import time
def many(n):
    start = time.time()
    #print("\n".format(i))
    subprocess.call("nextflow run nextRandJoinPresentation.nf --numberOfRands {}".format(n), shell=True)
    print('------------------------------\n Time {}'.format(time.time() - start))
if __name__ == '__main__':
    if (len(sys.argv) == 1):
        n = 10
    else:
        n = int(sys.argv[1])
    many(n)
