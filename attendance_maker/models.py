from django.db import models

# Create your models here.
"""
class record(models.Model):
    name=models.CharField(max_length=20)
    subject1=models.IntegerField(default=0)
    subject2=models.IntegerField(default=0)
    subject3=models.IntegerField(default=0)
    subject4=models.IntegerField(default=0)
    status=models.BooleanField(default=False)
    #students=Students.objects.all()

class IP(models.Model):
    address=models.CharField(max_length=30)
"""
class CLASS_CODE(models.Model):
    Code=models.CharField(max_length=20)

class Students_Record(models.Model):
    #Code=models.ForeignKey(CLASS_CODE,on_delete=models.CASCADE)
    Code=models.CharField(max_length=20)
    Student_Name=models.CharField(max_length=20)
    A=models.IntegerField(default=0)
    B=models.IntegerField(default=0)
    C=models.IntegerField(default=0)
    D=models.IntegerField(default=0)
    E=models.IntegerField(default=0)
    F=models.IntegerField(default=0)
    status=models.BooleanField(default=True)
    SubjectName=models.CharField(max_length=20)
    latitude=models.FloatField(default=-1)
    longitude=models.FloatField(default=-1)
    IP=models.CharField(max_length=30,default='#')
    Image=models.ImageField(upload_to='images/')
    Image_current=models.ImageField(upload_to='images/')

class Teachers_Record(models.Model):
    #Code=models.ForeignKey(CLASS_CODE,on_delete=models.CASCADE)
    Code=models.CharField(max_length=20)
    A=models.CharField(max_length=20)
    B=models.CharField(max_length=20)
    C=models.CharField(max_length=20)
    D=models.CharField(max_length=20)
    E=models.CharField(max_length=20)
    F=models.CharField(max_length=20)
    
class Subject_Information(models.Model):
    #Code=models.ForeignKey(CLASS_CODE,on_delete=models.CASCADE)
    Code=models.CharField(max_length=20)
    A=models.CharField(max_length=20)
    B=models.CharField(max_length=20)
    C=models.CharField(max_length=20)
    D=models.CharField(max_length=20)
    E=models.CharField(max_length=20)
    F=models.CharField(max_length=20)
    






