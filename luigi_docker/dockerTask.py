# -*- coding: utf-8 -*-

from collections import defaultdict
from heapq import nlargest

from luigi import six

import subprocess
import os
import luigi
import luigi.contrib.hadoop
import luigi.contrib.hdfs
import luigi.contrib.postgres

class DockerTaskCreate(luigi.Task):
    id = 1
    def output(self):
        return luigi.LocalTarget("dockerResults/imageID_{}.tsv".format(self.id))        
    def run(self):
        subprocess.call(["docker build -t dockerfile ."], shell=True)
        #os.system("clear")
        self.id = subprocess.check_output("docker images dockerfile --format \"{{.ID}}\"", shell=True)
        with self.output().open('w') as out_file:
            out_file.write(str(self.id))

class DockerTaskRun(luigi.Task):
    image = luigi.Parameter(default = "dockerfile")
    def requires(self):
        return [DockerTaskCreate()]
    def output(self):
        return luigi.LocalTarget("dockerResults/imageOutput_A.txt")
    def run(self):
        subprocess.call(["docker run -v /home/alex/luigi_docker:/home/luigi_docker dockerfile python hello.py"], shell=True)
        



class LuigiTask1(luigi.Task):
    x = luigi.IntParameter()
    y = luigi.IntParameter(default=55)
    
    
    def output(self):
        return luigi.LocalTarget("dataTest/task1_A_C.tsv")##.format(self.x, self.y))

    def requires(self):
        return []
    
    def run(self):
        with self.output().open('w') as out_file:
            for i in range(10):
                out_file.write('{}\t{}\t{}\n'.format(self.x, i, self.x*self.y))
    

class LuigiTask2(luigi.Task):
    x = luigi.IntParameter()
    y = luigi.IntParameter(default=55)
    
    def requires(self):
        return LuigiTask1(self.x, self.y)

    def output(self):
        return luigi.LocalTarget("dataTest/successReadWrite")
    
    def run(self):

        numbers = defaultdict(int)
        
        t = self.input()
        with t.open('r') as in_file:
            for line in in_file:
                num1, num2, mult = line.strip().split()
                numbers[num2] = int(mult)
        with self.output().open('w') as out_file:
            for num, count in six.iteritems(numbers):
                out_file.write('{}\t{}\n'.format(num, count))
    
##if __name__ == "__main__":
##    luigi.run()
