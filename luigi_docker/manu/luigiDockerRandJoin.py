#PYTHONPATH='.' luigi --module luigiRandJoin luigiJoinRandTask --intRange 175 --stringRange 145
import luigi
from randomNumber import randInt
from randString import randString
import os
import docker
from contextlib import contextmanager

client = docker.from_env()

class luigiCleanUp(luigi.Task):
    success = True
    def output(self):
        return luigi.LocalTarget('res/.deleted')
    def run(self):
        try:
            os.remove("res/randInts.txt")
            os.remove("res/randStrings.txt")
            os.remove('res/.deleted')
        except:
            self.success = False
        with self.output().open('w') as f:
            f.write('yes')

class luigiRandInts(luigi.Task):
    intRange = luigi.IntParameter(default = 100)
    def output(self):
        return luigi.LocalTarget('res/randInts_{}.txt'.format(self.intRange))

    def requires(self):
        return luigiCleanUp()

    def run(self):
        with self.output().open('w') as out:
            for i in randInt(self.intRange):
                out.write("{}\n".format(i))


class luigiRandStrings(luigi.Task):
    stringRange = luigi.IntParameter(default = 100)
    def output(self):
        return luigi.LocalTarget('res/randStrings_{}.txt'.format(self.stringRange))
    def requires(self):
        return luigiCleanUp()
    def run(self):
        with self.output().open('w') as fout:
            for num in range(self.stringRange):
                fout.write('{}\n'.format(randString()))

class luigiJoinRandTask(luigi.Task):
    stringRange = luigi.IntParameter(default = 100)
    intRange = luigi.IntParameter(default = 100)
    def output(self):
        return luigi.LocalTarget('res/randJoined_{}_{}.txt'.format(self.intRange, self.stringRange))
    def requires(self):
        return {'ints': luigiRandInts(self.intRange), 'strings': luigiRandStrings(self.stringRange)}
    def run(self):
        with self.input()['ints'].open('r') as fints:
            with self.input()['strings'].open('r') as fstrings:
                with self.output().open('w') as out:
                    for linei in fints:
                        out.write('{} = {}\n'.format(fstrings.readline().strip(), linei.strip()))
    def complete(self):
        return False

class multipleJoin(luigi.Task):
    def requires(self):
        return [luigiJoinRandTask(stringRange=x, intRange=x)
                    for x in range(100,200,10)]
    def run(self):
        print('Done')
