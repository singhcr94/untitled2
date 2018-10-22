from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class person(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=15)
    dob=models.DateField(max_length=8)
    phone=models.IntegerField()
    address=models.CharField(max_length=30)
    def __str__(self):
        return  self.firstname