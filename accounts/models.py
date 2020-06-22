
from django.db import models

# Create your models here.


class students(models.Model):
    name=models.CharField(max_length=20)
    latitude=models.FloatField(default=-1)
    longitude=models.FloatField(default=-1)

class teachers(models.Model):
    name=models.CharField(max_length=20)
    subject=models.CharField(max_length=20)
    latitude=models.FloatField(default=-1)
    longitude=models.FloatField(default=-1)



