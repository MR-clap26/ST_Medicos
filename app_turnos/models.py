from django.db import models
# Create your models here.

class ciudad(models.Model):
    nombre=models.CharField(max_length=60,null=False, blank=False)
    