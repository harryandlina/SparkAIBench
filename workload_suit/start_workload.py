import random
import information_FB
import sys
import os
import time
import subprocess

# 选择所需的各算法出现的比例，如不需要择填0

algorithm_MLlib = {"linear": 1, "als": 1, "kmeans": 1, "svm": 1, "bayes": 1, "FPGrowth": 1, "lda": 1}
algorithm_BigDL = {"lenet": 1, "resnet": 1, "rnn": 1, "vgg": 1, "autoencoder": 1}

# algorithm_MLlib =["linear", "als", "kmeans", "svm", "bayes", "FPGrowth", "lda"]
# algorithm_BigDL = ["lenet", "resnet", "rnn", "vgg", "autoencoder"]

jar_path = """/home/lzq/spark_jar/"""
output_path ="""/home/lzq/workload/workload_data/mnist"""

# 选择提交到spark上到队列名称和出现到比例大小

queue = {"queueA": 1, "queueB": 1}
all_algorithm = []
all_queue = []


def list_method_algorithm():
    for v, w in algorithm_MLlib.items():
        temp = []
        for i in range(w):
            temp.append(v)
        all_algorithm.extend(temp)
    for v, w in algorithm_BigDL.items():
        temp = []
        for i in range(w):
            temp.append(v)
        all_algorithm.extend(temp)


def list_method_queue():
    for v, w in queue.items():
        temp = []
        for i in range(w):
            temp.append(v)
        all_queue.extend(temp)

from threading import Thread

class Mythread(Thread):
    
    def __init__ (self,string):
        super().__init__()
        self.commond = string

    def run(self):
        subprocess.Popen(self.commond,shell=True)


if __name__ == '__main__':
    list_method_algorithm()
    list_method_queue()
    n = sys.argv[1]
    n = int(n)
   
    pathroot = os.path.abspath('.')
    information = information_FB.getinf(n, pathroot)


    for i in range(n):
        classname = all_algorithm[random.randint(0, len(all_algorithm) - 1)]
        queue = all_queue[random.randint(0, len(all_queue) - 1)]
        pathjar = jar_path + "workload_" + classname + ".jar"
        size = information[i][1]
        interval = information[i][0]
        queue = "queueB"
        commond_str = pathroot+"/start.sh "+classname+" "+queue+" "+pathjar+" "+str(size)+" "+output_path
        print(commond_str)
        print(interval)
        time.sleep(interval)
        # process = subprocess.Popen(commond_str,shell=True)
        threadtemp = Mythread(commond_str)
        threadtemp.start()
        print("next job\n")


    # start_BigDL.start_BigDL(algorithm_BigDL)
