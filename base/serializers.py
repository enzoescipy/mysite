from rest_framework import serializers
from .models import GPSTime

class GPSTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPSTime
        fields = ('id','lat', 'long','year', 'month','date','hour','minute','second')