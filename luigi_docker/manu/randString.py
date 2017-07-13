import random
import string
from time import sleep

def randString(x = 100):
    random.seed()
    sleep(0.1)
    return ''.join(random.choice(string.lowercase) for _ in range(random.randint(1,x)))

if __name__ == "__main__":
    print(randString())
