from django.db import models

# Create your models here.
class contact(models.Model):
    time=models.DateTimeField(auto_now_add=True)   
    fname=models.CharField(max_length=20)     
    lname=models.CharField(max_length=20)       
    phone_no=models.BigIntegerField()              
    email=models.EmailField()                   
    city=models.CharField(max_length=20)
    contact_reason=models.TextField()

class signup_master(models.Model):
    time=models.DateTimeField(auto_now_add=True)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    uname=models.CharField(max_length=30)
    email_id=models.EmailField()
    passwd=models.CharField(max_length=20)
    city_name=models.CharField(max_length=30)
    contact_no=models.BigIntegerField()

class basket(models.Model):
    itemname=models.CharField(max_length=30)
    itemprice=models.IntegerField()