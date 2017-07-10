#!/usr/bin/env nextflow
randints = Channel.create()
process cleanUp{
    '''
    '''
}

process randInts{
    output:
    file 'randInts.txt' into randints

    '''
    #!/usr/bin/python
    from random import randint
    import random
    from time import sleep
    lis = []
    n = 100
    random.seed()
    for i in range(n):
        sleep(0.5)
        lis.append(randint(1,n))
    with open('randInts.txt', 'w') as out:
        for num in lis:
            out.write('{}\\n'.format(num))
    '''
}

process randStrings{
    output:
    file 'randStrings.txt' into randstrings

    '''
    #!/usr/bin/python
from random import randint
import random
import string
from time import sleep
random.seed()
x = 100
with open('randStrings.txt', 'w') as out:
    for i in range(x):
        sleep(0.25)
        rstr = ''.join(random.choice(string.lowercase) for _ in range(randint(1,x)))
        out.write('{}\\n'.format(rstr))
    '''
}

process joinRandTask{
    input:
    file 'randInts.txt' from randints
    file 'randStrings.txt' from randstrings

    output:
    file 'randJoined.txt' into randjoined

    '''
    #!/usr/bin/python
with open('randInts.txt', 'r') as fints:
    with open('randStrings.txt', 'r') as fstrings:
        with open('randJoined.txt', 'w') as out:
            for linei in fints:
                out.write('{} = {}'.format(fstrings.readline().strip(), linei))
    '''
}
