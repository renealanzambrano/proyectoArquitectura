from django.db import models
from django.conf import settings
from django.utils import timezone
from django.shortcuts import render
# Create your models here.
class rfidTemp(models.Model):
    rfidTemp= models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.rfidTemp


    class Meta:
        db_table = 'rfidTemp'
