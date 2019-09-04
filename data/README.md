# SparkAIBench
Firstly, you should use produce_workload.sh to produce enough data files.

Secondly, you should put them in hdfs:/workload_data/
hadoop fs -mkdir /workload_data
hadoop fs -put yourdatapath /worload_data
