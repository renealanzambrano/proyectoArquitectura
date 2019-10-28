from django.db import models
from django.shortcuts import render
from django.db import models
from django.contrib.postgres.fields import JSONField
from django.conf import settings
from django.utils import timezone
from Alumno.models import Alumno
#Create your models here.
class Asistencia(models.Model):
    student= models.ForeignKey(Alumno, on_delete = models.SET(-1),null=True)
    fecha=models.DateTimeField(default = timezone.now)
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Asistencia'


