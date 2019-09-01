#!/usr/bin/env bash

#SPARK_HOME=/home/hadoop/sparkHadoopBigdl/spark
#hadoop_conf_dir=$3/etc/hadoop
#java_home=$4
#work_dir=$5
#queue=$6
#size=$7

#export JAVA_HOME=${java_home}
#export HADOOP_CONF_DIR=${hadoop_conf_dir}

class=$1
queue=$2
pathtojar=$3;
size=$4

if [ $5!="" ]; then
	pathtodata=$5;
fi



function submit() {
   

  #  spark_home =${SPARK_HOME}

    echo "Starting workload with parameters: class: ${class}, queue: ${queue}, data_size: ${size}"

    case ${class} in
    "rnn")
        
        spark-submit \
        --class com.intel.analytics.bigdl.models.${class}.workload_${class} \
            --master yarn \
            --deploy-mode cluster \
            --executor-cores 2 \
            --num-executors 2 \
            --executor-memory 6g \
            --driver-memory 2g \
            --queue ${queue} \
            ${pathtojar} \
            -b 8 \
            -f ${pathtodata} \
            -s ${pathtodata}/output \
            --checkpoint ${pathtodata}/output \
            -e ${size}

         rm -r ${pathtodata}/output/*
         ;;

    "autoencoder" | "lenet")
        
        spark-submit \
            --class com.intel.analytics.bigdl.models.${class}.workload_${class} \
            --master yarn \
            --deploy-mode cluster \
            --executor-cores 2 \
            --num-executors 2 \
            --executor-memory 6g \
            --driver-memory 2g \
            --queue ${queue} \
            ${pathtojar} \
            -b 8 \
            -f ${pathtodata} \
            -e ${size}
        ;;

    "resnet" | "vgg")
        
        spark-submit \
            --class com.intel.analytics.bigdl.models.${class}.workload_${class} \
            --master yarn \
            --deploy-mode cluster \
            --executor-cores 2 \
            --num-executors 2 \
            --executor-memory 6g \
            --driver-memory 2g \
            --queue ${queue} \
            ${pathtojar} \
            -b 8 \
            -f ${pathtodata}/cifar-10 \
            -e ${size}
        ;;
        
    *)

        spark-submit \
        --class ${class} \
        --master yarn \
        --deploy-mode cluster \
        --queue ${queue} \
        --num-executors 5 \
        --executor-cores 4 \
        --executor-memory 6g \
        --driver-memory 1g \
         ${pathtojar} ${size}
	;;
esac

}

submit ${class} ${queue} ${pathtojar} ${size} ${pathtodata}
