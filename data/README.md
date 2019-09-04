# SparkAIBench
Firstly, you should use produce_workload.sh to produce enough data files.
<br>
Secondly, you should put them in hdfs:/workload_data/
<br>
hadoop fs -mkdir /workload_data
<br>
hadoop fs -put yourdatapath /worload_data
