from random import randint
import random
from time import sleep

def randInt(n):
    #seed()
    lis = []
    random.seed()
    for i in range(n):
        sleep(0.1)
        lis.append(randint(1,n))
    return lis

if __name__ == "__main__":
    print(randInt())
