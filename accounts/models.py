
from django.db import models

# Create your models here.


class students(models.Model):
    name=models.CharField(max_length=20)

class teachers(models.Model):
    name=models.CharField(max_length=20)


