from django.db import models
from django.shortcuts import render
from django.db import models
from django.conf import settings
from django.utils import timezone
#from Asignatura.models import Asignatura

# Create your models here
class Registro(models.Model):
    fecha= models.DateTimeField(default = timezone.now)
    codigo=models.CharField(max_length=100, null=True)
    status=models.BooleanField(default=False)
    idalumno=models.CharField(max_length=10, null=True)
    def __str__(self):
        return self.name


    class Meta:
        db_table = 'registroRFID'
