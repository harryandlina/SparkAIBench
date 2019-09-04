# SparkAIBench
detail information could be found in :<br>
user manual : [harryandlina.github.io](harryandlina.github.io)
<br>
<br>

批量提交负载：<br>
```
python start_workload.py <number><br>
```
最后一个参数为提交作业的个数。<br>
<br>
单个提交负载：<br>
MLlib和BigDL负责都可以通过使用start.sh脚本调用运行<br>
MLlib提交实例如下：<br>
```
bash start.sh <algorithmname> <queue> <pathtojar> <size>
```
<br>
algorithmname选择提交的算法名称：linear， kmeans， svm， bayes ，FPGrowth，lda<br>
queue为提交到的队列名称<br>
pathjar输入jar的绝对路径<br>
size选择提交的数据量大小，可选范围为1-8，1代表数据量最小，8代表数据量最多<br>
<br>
<br>
BigDL提交实例如下：<br>

```
bash start.sh \<algorithmname> \<queue> \<pathtojar> \<iterationtime> \<pathtodata><br>
```
<br>
<br>
algorithmname选择需要的算法名称：rnn，autoencoder，lenet，resnet，vgg<br>
queue为提交到的队列名称<br>
pathtojar输入jar的绝对路径<br>
iterationtime选择迭代的次数<br>
pathtodata输入数据集所在的绝对路径<br>


