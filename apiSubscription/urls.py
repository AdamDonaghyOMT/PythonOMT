from django.conf.urls import url
from django.contrib import admin
from .views import subscribeGet, subscribePost, heartbeat, unsubscribePost

urlpatterns = [
    url(r'unsubscribe/(?P<email>[^/]+)', unsubscribePost),
 	url(r'subscribe/(?P<email>[^/]+)',   subscribePost),
 	url(r'subscribe/', subscribeGet),
    url(r'heartbeat/',   heartbeat),
]
