import json
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='xxx.xxx.xxx.xxx')
topic = 'asasa'

with open('test_2.json') as f:
    for line in f:
        producer.send(topic, line.encode('utf-8'))
