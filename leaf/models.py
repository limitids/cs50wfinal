from django.db import models

# Create your models here.


class zipToCoord(models.Model):
    zip = models.TextField()
    lat = models.TextField()
    long = models.TextField()