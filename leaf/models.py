from statistics import mode
from django.db import models

# Create your models here.


class zipToCoord(models.Model):
    zip = models.TextField()
    lat = models.TextField()
    long = models.TextField()


class Resturaunt(models.Model):
    address = models.TextField()
    name = models.TextField()
    long = models.TextField()
    lat = models.TextField()
    email = models.TextField()
    website = models.TextField()
    status = models.TextField()



class MenuItem(models.Model):
    resturaunt = models.ForeignKey(Resturaunt, on_delete=models.CASCADE)
    cost = models.IntegerField()
    description = models.TextField()
    title = models.TextField()