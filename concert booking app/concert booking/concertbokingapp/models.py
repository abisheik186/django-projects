from django.db import models
from django.contrib.auth.models import User
class concertslist( models.Model ): #titl,desc,artist,venue,date,availtckt,
    title=models.CharField(max_length=50)
    description=models.TextField()
    artist=models.CharField(max_length=50)
    venue=models.CharField(max_length=50)
    date=models.DateField()
    availticket=models.IntegerField()
class tcktbooking(models.Model):   #concerttitle,tcktcount,name,email
    name=models.CharField(max_length=50)
    email=models.EmailField()
    concerttitle=models.CharField(max_length=50)
    count=models.IntegerField()
class bookinghistory(models.Model):
    title=models.CharField(max_length=50)
    artist=models.CharField(max_length=50)
    venue=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    count=models.IntegerField()
    bookedtime=models.DateTimeField()