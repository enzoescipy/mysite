from django.db import models

class GPSTime(models.Model):
    id = models.IntegerField(primary_key=True)

    lat = models.CharField(max_length=200)
    long = models.CharField(max_length=200)

    year = models.IntegerField()
    month = models.IntegerField()
    date = models.IntegerField()
    hour = models.IntegerField()
    minute = models.IntegerField()
    second = models.IntegerField()