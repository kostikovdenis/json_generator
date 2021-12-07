import json
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='xxx.xxx.xxx.xxx')
topic = 'asasa'

with open('test_1.json') as f:
    data = json.load(f)
    producer.send(topic, data.encode('utf-8'))

