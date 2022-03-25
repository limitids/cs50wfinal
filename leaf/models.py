from statistics import mode
from django.db import models

# Create your models here.


class zipToCoord(models.Model):
    zip = models.TextField()
    lat = models.TextField()
    long = models.TextField()


class Resturaunt(models.Model):
    lat = models.TextField()
    long = models.TextField()
    name = models.TextField()
    rating = models.IntegerField()
    email = models.IntegerField()



class MenuItem(models.Model):
    resturaunt = models.ForeignKey(Resturaunt, on_delete=models.CASCADE)
    cost = models.IntegerField()
    description = models.TextField()
    title = models.TextField()