from kafka import KafkaProducer

pd = KafkaProducer(bootstrap_servers='localhost:9092')

pd.send('test', b'hello2')
pd.flush()