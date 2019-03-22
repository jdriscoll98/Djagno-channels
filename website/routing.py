from django.conf.urls import url

from . import consumers

# this is the urls.py of Channels

websocket_urlpatterns = [
    url(r'^ws/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
]
