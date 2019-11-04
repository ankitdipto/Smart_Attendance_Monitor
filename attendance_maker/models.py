from django.db import models

# Create your models here.
class record(models.Model):
    name=models.CharField(max_length=20)
    subject1=models.IntegerField(default=0)
    subject2=models.IntegerField(default=0)
    subject3=models.IntegerField(default=0)
    #students=Students.objects.all()