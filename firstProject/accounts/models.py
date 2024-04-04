from django.db import models

# Create your models here.
class acc(models.Model):
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
