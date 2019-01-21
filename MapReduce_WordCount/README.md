# Python-MapReduce-WordCount
To run this code one should first configure its cluster within the HADOOP enviroment, by configuring all the relevant files.

It can be done within a Windows operative system if one uses a Virtual Machine to emulate a Linux enviroment, in which a 
stable version of HADOOP and the Java Virtual Machine are installed.

I would like to refer any readers to Lazy Programmer's book "Big Data, Mapreduce, Hadoop and Spark with Python"
from which I took this example, and where the configuration of HADOOP is detally explained.

Once the cluster structure is done (ports, slaves nodes and master node are correctly identified in the 
relevant scripts as yarn-site, core-site, etc...), it is possible to start the Hadoop Distributed File System (HDFS) which 
is where our files will live in:

    user@server~$ $HADOOP_HOME/sbin/start-dfs.sh

Afterwards it is time to launch the YARN daemons, which are the processes that will allow the parallel processing:

    user@server~$ $HADOOP_HOME/sbin/start-yarn.sh

Now, let's load the flat text file onto which we will perform our word-counting in the HADOOP Distributed File System. In this case, the
that text file will be Spanish novel "El Quijote". This is achieved providing, after de command -put, the local file path and 
then, the HDFS path:

    user@server~$ $HADOOP_HOME/bin/hdfs dfs -put /opt/datasets/txt/el_quijote.txt /datasets/txt

Finally, we need to espcify mapper and reducer paths, tell HADOOP which of these files is the mapper and which is the reducer,
provide an input and also and output 

    user@server~$ $HADOOP_HOME/bin/hadoop jar /opt/hadoop-2.7.7/share/hadoop/tools/lib/hadoop-streaming-2.7.7.jar \
    -files /opt/HadoopMR/mapper.py,/opt/HadoopMR/reducer.py \
    -mapper mapper.py -reducer reducer.py \
    -input /datasets/txt/el_quijote.txt -output /datasets/txt/el_quijote_wordcount
    
 Obviusly there are pretty simplier ways of doing things, especially using SPARK project which also works onto the HADOOP file 
 distribution but provides APIs for several programming languages (i.e. Python and Scala), and features also an easier 
 installation and configuration.

