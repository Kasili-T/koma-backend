from django.urls import re_path

# Import consumers lazily inside list comprehension
websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_id>\w+)/$', __import__('chat.consumers').consumers.ChatConsumer.as_asgi()),
]
