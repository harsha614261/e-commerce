from django.db import models

# Create your models here.

class upload(models.Model):
    objects=models.Manager()
    img=models.ImageField(upload_to ='uploads/')
    Cname = models.CharField(max_length=100)
    CInstructor = models.CharField(max_length=100)
    Cduration = models.CharField(max_length=100)
    Ctopics = models.CharField(max_length=100)
    Accessibility = models.CharField(max_length=100)
    Cost = models.IntegerField()
class Cart(models.Model):
    objects=models.Manager()
    uid = models.IntegerField()
    img = models.ImageField(upload_to='uploads/')
    Cname = models.CharField(max_length=100)
    CInstructor = models.CharField(max_length=100)
    Cduration = models.CharField(max_length=100)
    Ctopics = models.CharField(max_length=100)
    Accessibility = models.CharField(max_length=100)
    Cost = models.IntegerField()
class MyOrder(models.Model):
    objects=models.Manager()
    uname=models.CharField(max_length=100)
    mail=models.CharField(max_length=100)
    pid=models.IntegerField()
    status=models.CharField(max_length=1000)

class queries(models.Model):
    objects=models.Manager()
    Name=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Number=models.IntegerField()
    Message=models.CharField(max_length=1000)