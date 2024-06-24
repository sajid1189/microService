import logging
import pika
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.core.management import BaseCommand

logger = logging.getLogger(__name__)


def send(ch, method, properties, body):
    channel_layer = get_channel_layer()
    message = f"created data: {body}"
    print(f"received {message}")
    async_to_sync(channel_layer.group_send)(
        "data_notification",
        {
            "type": "chat_message",
            "message": message,
        },
    )
    ch.basic_ack(delivery_tag=method.delivery_tag)



class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()

        channel.queue_declare(queue='data_notification', durable=True)
        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue='data_notification', on_message_callback=send)

        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()

        print("Channel stopped consuming")
