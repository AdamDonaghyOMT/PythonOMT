from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Event
from .serializers import UserSerializer, EventSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


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


class unsubscribe(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        return JsonResponse({"Message":"get not supported at this end point"}, status=404)# is this the correct  error code?


    def post(self, request, format=None):
    	#Expect to get some stuff to over write a current one
    	#Do a get over the top of this stuff 
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class subscribe(APIView):
    """
    Create a new subscription
    """
   
    def get(self, request, format=None):
    	#filter to only show what that user is subscribed to
        snippets = Event.objects.all()
        serializer = EventSerializer(snippets, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() #create a new instance of the event
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)