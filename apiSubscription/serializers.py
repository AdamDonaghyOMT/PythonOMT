from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from .models import Event

# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

#Serializers to defin the API representation fo
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('title', 'ownerUser', 'triggerPrice', 'asx_code', 'frequency')

