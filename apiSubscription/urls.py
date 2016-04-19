from django.conf.urls import url
from django.contrib import admin
from .views import unsubscribe, subscribe, heartbeat

urlpatterns = [
    url(r'unsubscribe/', unsubscribe.as_view()),
 	url(r'subscribe/',   subscribe.as_view()),
    url(r'heartbeat/',   heartbeat),
]
