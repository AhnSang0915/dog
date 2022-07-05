import email
from django.db import models
from django.forms import CharField, EmailField, IntegerField

# Create your models here.

class Owners(models.Model):
    name = models.CharField(max_length=45, null=True) 
    email = models.EmailField(max_length=254)
    age = models.IntegerField()
    
    class Meta:
        db_table = 'Owners'

class Dogs(models.Model):
    owner = models.ForeignKey('Owners', on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    age = models.IntegerField()

    class Meta:
        db_table = 'Dogs'