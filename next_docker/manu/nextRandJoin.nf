#!/usr/bin/env nextflow

params.intRange = 100
params.stringRange = 100

process cleanUp{
    '''
    '''
}

process randInts{
    output:
    file "randInts_${params.intRange}.txt" into randints

    """
    #!/usr/bin/python
    from random import randint
    import random
    from time import sleep
    lis = []
    n = ${params.intRange}
    random.seed()
    for i in range(n):
        #sleep(0.5)
        lis.append(randint(1,n))
    with open('randInts_{}.txt'.format(n), 'w') as out:
        for num in lis:
            out.write('{}\\n'.format(num))
    """
}

process randStrings{
    output:
    file "randStrings_${params.stringRange}.txt" into randstrings

    """
    #!/usr/bin/python
    from random import randint
    import random
    import string
    from time import sleep
    random.seed()
    x = ${params.stringRange}
    with open('randStrings_{}.txt'.format(x), 'w') as out:
        for i in range(x):
            #sleep(0.25)
            rstr = ''.join(random.choice(string.lowercase) for _ in range(randint(1,x)))
            out.write('{}\\n'.format(rstr))
    """
}

process joinRandTask{
    input:
    file randints from randints
    file randstrings from randstrings

    output:
    file "randJoined_${params.intRange}_${params.stringRange}.txt" into randjoined

    """
    #!/usr/bin/python
    intRange = ${params.intRange}
    stringRange = ${params.stringRange}
    with open('${randints}', 'r') as fints:
        with open('${randstrings}', 'r') as fstrings:
            with open('randJoined_{}_{}.txt'.format(intRange,stringRange), 'w') as out:
                for linei in fints:
                    out.write('{} = {}'.format(fstrings.readline().strip(), linei))
    """
}
