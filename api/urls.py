from django.conf.urls import url
from django.contrib import admin
from .views import unsubscribe, subscribe, heartbeat, EventList

urlpatterns = [
    url(r'unsubscribe/', EventList.as_view()),
 	url(r'subscribe/',   subscribe),
    url(r'heartbeat/',   heartbeat),
]
