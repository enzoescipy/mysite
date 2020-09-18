from rest_framework.response import  Response
from rest_framework.decorators import api_view
from .models import GPSTime
from .serializers import GPSTimeSerializer
from rest_framework import status

@api_view(['GET'])
def datashower(request):
    totaldatas = GPSTime.objects.all()
    serializer = GPSTimeSerializer(totaldatas, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def dataposter(request):
    serializer = GPSTimeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def datadeleter(request, id):
    instance = GPSTime.objects.get(id=id)
    instance.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)