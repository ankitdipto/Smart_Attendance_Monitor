from django.db import models

# Create your models here.
class record(models.Model):
    name=models.Charfield(max_length=20)
    subject1=models.Integerfield(default=0)
    subject2=models.Integerfield(default=0)
    subject3=models.Integerfield(default=0)
    #students=Students.objects.all()