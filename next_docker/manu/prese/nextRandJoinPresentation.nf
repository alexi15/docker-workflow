#!/usr/bin/env nextflow

params.intRange = 0
params.stringRange = 0
params.numberOfRands = 100

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
    n = ${params.intRange}
    with open('randInts_{}.txt'.format(n), 'w') as out:
        lis = []
        random.seed()
        for i in range(${params.numberOfRands}):
            lis.append(randint(1000000,9999999))
        for i in lis:
            out.write('{}\\n'.format(i))
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
        for i in range(${params.numberOfRands}):
            randstr = ''.join(random.choice(string.lowercase) for _ in range(50))
            out.write('{}\\n'.format(randstr))
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
