import json

from django.http import HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from .models import Event
from .serializers import UserSerializer, EventSerializer

#JSON RESPONSE FOR API END POINTS
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)



def heartbeat(request):
	pass


@api_view(['POST'])
def unsubscribePost(self, request, email=None, format=None):
	#Expect to get some stuff to over write a current one
	#Do a get over the top of this stuff
    """
    Post: Delete an event subscription for a given user
    """
    data = json.loads(request.body)
    asx_code = data['asx_code']

    if email is not None and asx_code is not None:
        unsubscribeEvent = Event.objects.get(email=email, asx_code=asx_code)
        unsubscribe.delete()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def subscribeGet(self, request, format=None):
	#filter to only show what that user is subscribed to
    """
        Get: All the current subscriptions of a user \n
    """
    snippets = Event.objects.all()
    serializer = EventSerializer(snippets, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def subscribePost(self, request, format=None):
    """
    Post: Create a new subscription
    """
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save() #create a new instance of the event
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


