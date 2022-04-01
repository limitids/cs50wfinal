from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class zipToCoord(models.Model):
    zip = models.TextField()
    lat = models.TextField()
    long = models.TextField()


class Resturaunt(models.Model):
    address = models.TextField()
    name = models.TextField()
    long = models.FloatField()
    lat = models.FloatField()
    email = models.TextField()
    website = models.TextField()
    status = models.TextField()
    creator = models.ForeignKey(User,on_delete=models.CASCADE)



class MenuItem(models.Model):
    resturaunt = models.ForeignKey(Resturaunt, on_delete=models.CASCADE)
    cost = models.IntegerField()
    description = models.TextField()
    title = models.TextField()
    img = models.URLField(default='')