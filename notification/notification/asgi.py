"""
ASGI config for notification project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

from notify import routing


import os

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from django.urls import path

from notify.consumers import ChatConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notifications.settings')

application = ProtocolTypeRouter({
  'http': get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter([
            path("ws/notifications/", ChatConsumer.as_asgi()),
        ])
    ),
})