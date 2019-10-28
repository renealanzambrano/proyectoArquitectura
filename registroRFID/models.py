from django.db import models
from django.shortcuts import render
from django.db import models
from django.contrib.postgres.fields import JSONField
from django.conf import settings
from django.utils import timezone
#from Asignatura.models import Asignatura

# Create your models here
class Registro(models.Model):
    rfid=models.CharField(max_length=50, null=True),
    fecha= models.DateTimeField(default = timezone.now),
    exist=models.BooleanField (default = False),
    
    def __str__(self):
        return self.name


    class Meta:
        db_table = 'registroRFID'