#PYTHONPATH='.' luigi --module luigiRandJoin luigiJoinRandTask --intRange 175 --stringRange 145
import luigi
import os
import random
from random import randint
import string



class luigiCleanUp(luigi.Task):
    success = True
    def output(self):
        return luigi.LocalTarget('.deleted')
    def run(self):
        try:
            os.remove("randInts.tsv")
            os.remove("randStrings.tsv")
            os.remove('.deleted')
        except:
            self.success = False
        with self.output().open('w') as f:
            f.write('yes')

class luigiRandInts(luigi.Task):
    intRange = luigi.IntParameter(default = 0)
    numberOfRands = luigi.IntParameter(default = 100)
    def output(self):
        return luigi.LocalTarget('res/randInts_{}.tsv'.format(self.intRange))

    def requires(self):
        return luigiCleanUp()

    def run(self):
        with self.output().open('w') as out:
            lis = []
            n = self.intRange
            random.seed()
            for i in range(n):
                lis.append(randint(1000000,9999999))
            for i in lis:
                out.write("{}\n".format(i))

class luigiRandStrings(luigi.Task):
    stringRange = luigi.IntParameter(default = 0)
    numberOfRands = luigi.IntParameter(default = 100)
    def output(self):
        return luigi.LocalTarget('res/randStrings_{}.txt'.format(self.stringRange))
    def requires(self):
        return luigiCleanUp()
    def run(self):
        random.seed()
        x = self.stringRange
        with self.output().open('w') as fout:
            for num in range(self.numberOfRands):
                randString = ''.join(random.choice(string.lowercase) for _ in range(50))
                fout.write('{}\n'.format(randString))

class luigiJoinRandTask(luigi.Task):
    stringRange = luigi.IntParameter(default = 100)
    intRange = luigi.IntParameter(default = 100)
    numberOfRands = luigi.IntParameter(default = 100)
    def output(self):
        return luigi.LocalTarget('res/randJoined_{}_{}.txt'.format(self.intRange, self.stringRange))
    def requires(self):
        return {'ints': luigiRandInts(self.intRange, self.numberOfRands), 'strings': luigiRandStrings(self.stringRange, self.numberOfRands)}
    def run(self):
        with self.input()['ints'].open('r') as fints:
            with self.input()['strings'].open('r') as fstrings:
                with self.output().open('w') as out:
                    for linei in fints:
                        out.write('{} = {}\n'.format(fstrings.readline().strip(), linei.strip()))
    def complete(self):
        return False
