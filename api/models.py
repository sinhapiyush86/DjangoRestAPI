from django.db import models

# Create your models here.
class Temperature(models.Model):
    tempdata = models.IntegerField()
