
import pika
import json


def notify_data_creation(message: str):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='data_notification', durable=True)
    channel.basic_publish(
        exchange='',
        routing_key='data_notification',
        body=message,
        properties=pika.BasicProperties(delivery_mode=2)  # Make message persistent
    )

    print(f" [x] Sent {message}")
    connection.close()

