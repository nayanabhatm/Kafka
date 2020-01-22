from kafka import KafkaProducer,KafkaConsumer
import json
import os



bootstraps=['localhost:9092']
 #writes the message to kafka topic as bytes
producer = KafkaProducer(bootstrap_servers=bootstraps)

#writes the message in json format
json_producer = KafkaProducer(bootstrap_servers=bootstraps,value_serializer=lambda v: json.dumps(v).encode('utf-8'))

producer.send('testpartition1',b'\n.......raw_bytes')
producer.send('testpartition1',b'\n...........hello this is cool')

json_producer.send('testpartition1',{'....foo':'bar'})
json_producer.send('testpartition1',{'...key':'value'})

producer.close()
json_producer.close()


