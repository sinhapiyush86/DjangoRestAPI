from django.db import models

# Create your models here.
class Temperature(models.Model):
    tempdata = models.IntegerField()
    time = models.CharField(max_length=30)
    date = models.CharField(max_length=30)
    location = models.CharField(max_length=100)
