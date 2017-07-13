import random
import string
from time import sleep
import sys

def randString(stringRange, f):
    random.seed()
    #sleep(0.1)
    with open(f, 'w') as fout:
        for num in range(stringRange):
            st = ''.join(random.choice(string.lowercase) for _ in range(random.randint(1,stringRange)))
            fout.write('{}\n'.format(st))

    return f

if __name__ == "__main__":
    print(randString(int(sys.argv[1]), sys.argv[2]))
