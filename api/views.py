from django.http import HttpResponse
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



def unsubscribe(request):
	print('GOT TO THE PRINT')
	return HttpResponse(status=404)


@csrf_exempt
def subscribe(request):
	print('GOT TO THE subscribe')
	print(request)
	if request.method == "POST":
		data = JSONParser().parse(request.POST)
		serializer = EventSerializer(data=request.data)

		return JSONResponse(serializer.data, status=201)
	
	else:
			return HttpResponse(status=404)



def heartbeat(request):
	pass



class EventList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Event.objects.all()
        serializer = EventSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)