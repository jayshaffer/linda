from __future__ import unicode_literals

from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=200)
    lat = models.IntegerField(default=0)
    long = models.IntegerField(default=0)
    code = models.CharField(max_length=10)

class Temperature(models.Model):
    location = models.ForeignKey(Location)
    reading = models.DecimalField(default=0.0, decimal_places=2, max_digits=4)
    date = models.DateTimeField(auto_now_add=True)

class Humidity(models.Model):
    location = models.ForeignKey(Location)
    reading = models.DecimalField(default=0.0, decimal_places=2, max_digits=4)
    date = models.DateTimeField(auto_now_add=True)
