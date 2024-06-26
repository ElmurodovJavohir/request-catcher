import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class DomainConsumer(WebsocketConsumer):
    def connect(self):
        self.domain = self.scope["url_route"]["kwargs"]["domain"]
        async_to_sync(self.channel_layer.group_add)(self.domain, self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(self.domain, self.channel_name)

    # Receive message from WebSocket
    # def receive(self, text_data):
    #     text_data_json = json.loads(text_data)
    #     message = text_data_json["message"]

    #     # Send message to room group
    #     async_to_sync(self.channel_layer.group_send)(
    #         self.domain, {"type": "chat_message", "message": message}
    #     )

    # # Receive message from room group
    def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message}))
