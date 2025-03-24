from django.urls import re_path

from core.consumer import FaceConsumer

websocket_urlpatterns = [
    re_path(r"ws/faces/?$", FaceConsumer.as_asgi()),
]