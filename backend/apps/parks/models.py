
from django.db import models

class DogPark(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    lat = models.FloatField()
    lng = models.FloatField()
