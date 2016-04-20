from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from .views import subscriptions, heartbeat

urlpatterns = [
 	url(r'subscribe/(?P<email>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$',   subscriptions),
    url(r'heartbeat/',   heartbeat),
]
