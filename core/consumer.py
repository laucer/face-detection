from channels.generic.websocket import AsyncWebsocketConsumer
import json

class FaceConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("face_group", self.channel_name)
        await self.accept()

    async def disconnect(self, _):
        await self.channel_layer.group_discard("face_group", self.channel_name)

    async def send_url(self, event):
        await self.send(text_data=json.dumps({"url": event["url"]}))