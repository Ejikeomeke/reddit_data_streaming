# To stream data to kafka producer
def stream_data(data):
    from kafka import KafkaProducer
    import time
    import json
    import logging
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'], max_block_ms=5000)
    curr_time = time.time()
    while True:
            if time.time() > curr_time + 60: #1 minute
                break
            try:

                producer.send('omekedata', json.dumps(data).encode('utf-8'))
            except Exception as e:
                logging.error(f'An error occured: {e}')
                continue

