from pyspark import SparkContext,SparkConf
from pyspark.sql import SparkSession,SQLContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

spark=SparkSession.builder.appName('sparkstreaming_khafka').getOrCreate()
sc=spark.sparkContext
ssc=StreamingContext(sc,1)

zookeeper_ipaddr="localhost:2182"
topic_name='testnbm'
consumer_name=topic_name+'_Consumer'

kvs=KafkaUtils.createStream(ssc,zookeeper_ipaddr,consumer_name,{topic_name:1})
lines=kvs.map(lambda x:x[1])
lines.pprint()

ssc.start()
ssc.awaitTermination()
