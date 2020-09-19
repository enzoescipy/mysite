from rest_framework.response import  Response
from rest_framework.decorators import api_view
from .models import GPSTime
from .serializers import GPSTimeSerializer
from rest_framework import viewsets

class GPSTimeViewSet(viewsets.ModelViewSet):
    queryset = GPSTime.objects.all()
    serializer_class = GPSTimeSerializer
