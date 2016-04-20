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


@api_view(['GET', 'POST', 'DELETE'])
def subscriptions(request, email=None, format=None):
	#filter to only show what that user is subscribed to
    """
    Endpoint to manage subscriptions 

    Get: All the current subscriptions of a user 
    Post: Create a new subscription '{ "triggerPrice": float , "frequency": int , "asx_code": 3 char }' 
    Delete: Deletes an event for a person given they've got '{"asx_code": 3 char}' 
    """
    if email is None:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        owenerEvents = Event.objects.filter(ownerEmail = email)
        serializer = EventSerializer(owenerEvents, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        request.data['ownerEmail'] = email
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid(): #get this for free from the event serializer
            serializer.save() #create a new instance of the event
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        data = json.loads(request.body)
        asx_code = data['asx_code']
        if asx_code is not None:
            try:
                unsubscribeEvent = Event.objects.filter(ownerEmail=email, asx_code=asx_code)
                unsubscribeEvent.delete() #delete first element if there are multiple     
                return Response(status=status.HTTP_200_OK)
            except:
                Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


