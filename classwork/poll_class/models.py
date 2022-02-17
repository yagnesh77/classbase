from django.db import models
from django.contrib import admin
# Create your models here.
class Person(models.Model):
    username = models.CharField(max_length = 200, unique = True)
    firstName = models.CharField(max_length = 200)
    middleName = models.CharField(max_length = 200)
    lastName = models.CharField(max_length = 200)
    age = models.IntegerField(default = 0)