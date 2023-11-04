from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from telemetry import consumers

websocket_urlpatterns = [
    path('ws/telemetry/', consumers.TelemetryConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    'websocket': URLRouter(websocket_urlpatterns)
})
