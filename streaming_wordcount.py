import findspark
findspark.init()

import os
from pyspark import SparkContext,SparkConf
from pyspark.sql import SparkSession, SQLContext
from pyspark.streaming import StreamingContext

sc = SparkContext("local[2]","streaming_wordcount")
ssc = StreamingContext(sc,1)

lines = ssc.socketTextStream("localhost",44444)

words=lines.flatMap(lambda line: line.split(" "))

pairs = words.map(lambda word:(word,1))
wordcounts = pairs.reduceByKey(lambda x,y: x+y)

wordcounts.pprint()


ssc.start()
ssc.awaitTermination()


