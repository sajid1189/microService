import logging
import pika
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.core.management import BaseCommand

logger = logging.getLogger(__name__)


def send(ch, method, properties, body):
    channel_layer = get_channel_layer()
    print(f"received message {body}")
    async_to_sync(channel_layer.group_send)(
        "data_notifications",
        {
            "type": "chat_message",
            "message": body,
        },
    )


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        print(f"sending message")
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "data_notification",
            {
                "type": "chat_message",
                "message": "body",
            },
        )
