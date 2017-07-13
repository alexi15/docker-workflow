#PYTHONPATH='.' luigi --module luigiRandJoin luigiJoinRandTask --intRange 175 --stringRange 145
import luigi
import os
import docker
from contextlib import contextmanager

from randomNumber import randInt
from randomString import randString
from joinRandomNumbersToStrings import joinThem

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
    imageName = luigi.Parameter(default = "myimage")
    out_path = 'res/{}_randInts.txt'
    def output(self):
        return luigi.LocalTarget(self.out_path.format(self.intRange))

    def requires(self):
        return luigiCleanUp()

    def run(self):
        container = client.containers.run(self.imageName,
            command = "python randomNumber.py {} {}".format(self.intRange, self.out_path.format(self.intRange)),
            volumes = {'/home/alex/docker-workflow/luigi_docker/manu_docker':
                                {'bind': '/home', 'mode': 'rw'}})
        #
        #randInt(self.intRange, self.output())
        #with self.output().open('w') as out:
        #    for i in randInt(self.intRange):
        #        out.write("{}\n".format(i))

class luigiRandStrings(luigi.Task):
    stringRange = luigi.IntParameter(default = 100)
    imageName = luigi.Parameter(default = "myimage")
    out_path = 'res/{}_randStrings.txt'
    def output(self):
        return luigi.LocalTarget(self.out_path.format(self.stringRange))

    def requires(self):
        return luigiCleanUp()

    def run(self):
        container = client.containers.run(self.imageName,
            command = "python randomString.py {} {}".format(self.stringRange, self.out_path.format(self.stringRange)),
            volumes = {'/home/alex/docker-workflow/luigi_docker/manu_docker':
                                {'bind': '/home', 'mode': 'rw'}})
        #randString(self.stringRange, self.output())
        # with self.output().open('w') as fout:
        #     for num in range(self.stringRange):
        #         fout.write('{}\n'.format(randString()))

class luigiJoinRandTask(luigi.Task):
    stringRange = luigi.IntParameter(default = 100)
    intRange = luigi.IntParameter(default = 100)
    imageName = luigi.Parameter(default = "myimage")
    def output(self):
        return luigi.LocalTarget('res/{}_{}_randJoined.txt'.format(self.intRange, self.stringRange))
    def requires(self):
        return {'ints': luigiRandInts(self.intRange, self.imageName), 'strings': luigiRandStrings(self.stringRange, self.imageName)}
    def run(self):
        container = client.containers.run(self.imageName,
            command = "python joinRandomNumbersToStrings.py {} {} {}"
                .format(
                'res/{}_randInts.txt'.format(self.intRange),
                'res/{}_randStrings.txt'.format(self.stringRange),
                'res/{}_{}_randJoined.txt'.format(self.intRange, self.stringRange)),
            #command = "echo Hello World > res.txt",
            volumes = {'/home/alex/docker-workflow/luigi_docker/manu_docker':
                                {'bind': '/home', 'mode': 'rw'}}
            )

        #joinThem(self.input()['ints'], self.input()['strings'], self.output())
        # with self.input()['ints'].open('r') as fints:
        #     with self.input()['strings'].open('r') as fstrings:
        #         with self.output().open('w') as out:
        #             for linei in fints:
        #                 out.write('{} = {}\n'.format(fstrings.readline().strip(), linei.strip()))

class multipleJoin(luigi.Task):
    def requires(self):
        return [luigiJoinRandTask(stringRange=x, intRange=x)
                    for x in range(100,200,10)]
    def run(self):
        print('Done')
