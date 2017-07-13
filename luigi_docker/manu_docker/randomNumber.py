from random import randint
import random
from time import sleep
import sys

def randInt(n,f):
    #seed()
    #f = file('{}_randInts.txt'.format(n))
    lis = []
    random.seed()
    for i in range(n):
        #sleep(0.1)
        lis.append(randint(1,n))
    #with f.open('w') as out:
    with open(f, 'w') as out:
        for i in lis:
            out.write("{}\n".format(i))
        return out

if __name__ == "__main__":
    print(randInt(int(sys.argv[1]), sys.argv[2]))
