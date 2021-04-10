from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    birthdate = models.DateField(null=True, blank=True)
    roll = models.CharField(max_length=10)
    password = models.CharField(max_length=100)
