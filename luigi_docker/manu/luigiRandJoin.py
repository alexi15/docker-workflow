import luigi
from randomNumber import randInt
from randString import randString
import os
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
    intRange = luigi.IntParameter(default = 100)
    def output(self):
        return luigi.LocalTarget('randInts.tsv')

    def requires(self):
        return luigiCleanUp()

    def run(self):
        with self.output().open('w') as out:
            for i in randInt(self.intRange):
                out.write("{}\n".format(i))

class luigiRandStrings(luigi.Task):
    stringRange = luigi.IntParameter(default = 100)
    def output(self):
        return luigi.LocalTarget('randStrings.txt')
    def requires(self):
        return luigiCleanUp()
    def run(self):
        with self.output().open('w') as fout:
            for num in range(self.stringRange):
                fout.write('{}\n'.format(randString()))

class luigiJoinRandTask(luigi.Task):
    def output(self):
        return luigi.LocalTarget('randJoined.txt')
    def requires(self):
        return {'ints': luigiRandInts(), 'strings': luigiRandStrings()}
    def run(self):
        with self.input()['ints'].open('r') as fints:
            with self.input()['strings'].open('r') as fstrings:
                with self.output().open('w') as out:
                    for linei in fints:
                        out.write('{} = {}\n'.format(fstrings.readline().strip(), linei.strip()))
