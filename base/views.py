from rest_framework.response import  Response
from rest_framework.decorators import api_view
from .models import GPSTime
from .serializers import GPSTimeSerializer

@api_view(['GET'])
def datashower(request):
    totaldatas = GPSTime.objects.all()
    serializer = GPSTimeSerializer(totaldatas, many=True)
    return Response(serializer.data)