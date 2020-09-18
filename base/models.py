from django.db import models

class GPSTime(models.Model):
    lat = models.DecimalField(decimal_places=8, max_digits=10)
    long = models.DecimalField(decimal_places=8, max_digits=10)

    year = models.IntegerField()
    month = models.IntegerField()
    date = models.IntegerField()
    hour = models.IntegerField()
    minute = models.IntegerField()
    second = models.IntegerField()