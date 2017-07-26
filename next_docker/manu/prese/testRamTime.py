import subprocess
import sys
import time

def testRam():
    for i in range(1000000,10000000,1000000):
        subprocess.call('/usr/bin/time -f "%E %P %M"  --output=time.txt --append python many.py {}'.format(i), shell=True)

if __name__ == '__main__':
    if (len(sys.argv) == 1):
        n = 10
    else:
        n = int(sys.argv[1])
    testRam()
