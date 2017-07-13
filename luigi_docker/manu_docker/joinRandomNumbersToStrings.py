from random import randint
import random
from time import sleep
import sys

def joinThem(file_ints, file_strings, file_out):
    with open(file_ints,'r') as ints:
        with open(file_strings,'r') as strings:
            with open(file_out, 'w') as out:
                for curr_int in ints:
                    out.write('{} = {}\n'.format(strings.readline().strip(), curr_int.strip()))
    return file_out

if __name__ == "__main__":
    print(joinThem(sys.argv[1], sys.argv[2], sys.argv[3]))
