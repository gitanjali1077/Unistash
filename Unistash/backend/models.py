from __future__ import unicode_literals
from django import forms
from django.db import models

# Create your models here.
class users(models.Model):
    username = models.CharField(max_length=200)
    #password = models.CharField(max_length=200)
    email= models.EmailField(max_length=200)
    college= models.CharField(max_length=200)

    def __str__(self):
        return self.username

   
class contactus(models.Model):
    email = models.EmailField(max_length=200)
    #password = models.CharField(max_length=200)
    subject= models.CharField(max_length=300)
    message= models.CharField(max_length=600)

    def __str__(self):
        return self.email
