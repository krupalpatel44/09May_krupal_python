from django.db import models
from .models import *

# Create your models here.

class registerdata(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    mobile=models.BigIntegerField()
    dob=models.DateField()
    city=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    address=models.TextField()
    aadhar=models.BigIntegerField()
    familytype=models.CharField(max_length=20)
    image=models.FileField(upload_to='Image/Members Photos/',default='/static/img/userprofile.png')
    
class watchman(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField()
    dob=models.DateField()
    mobile=models.BigIntegerField()
    aadhar=models.BigIntegerField()
    gender=models.CharField(max_length=20)
    image=models.FileField(upload_to='Image/watchman Photos/',default='/static/img/watchmanprofile.png')

class noticedata(models.Model):
    created_at=models.DateField(auto_now_add=True)
    charges_type=models.CharField(max_length=100)
    member_name=models.CharField(max_length=100)
    amount=models.IntegerField()
    inv=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    email=models.EmailField()
    discription=models.TextField()


class eventdata(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    event_title=models.CharField(max_length=100)
    event_img=models.ImageField(upload_to='profile_img')
    start_date=models.DateField()
    end_date=models.DateField()
    start_time=models.TimeField()
    end_time=models.TimeField()
    description=models.CharField(max_length=200)
