from django.db import models
from django.shortcuts import render
from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Alumno(models.Model):
    name= models.CharField(max_length=50, null=True)
    ap_pat= models.CharField(max_length=50, null=True)
    ap_mat= models.CharField(max_length=50, null=True)
    #edad= models.IntegerField(null=False)
    #address= models.CharField(max_length=50, null=True)
    #correo= models.CharField(max_length=50, null=True)
    #genero= models.CharField(max_length=50, null=True)
    #teacher=models.ForeignKey(Profesor, on_delete = models.SET(-1),null=True)
    fecha=models.DateTimeField(default = timezone.now)
    idrfid=models.CharField(max_length=10, null=True)
    def __str__(self):
        return self.name


    class Meta:
        db_table = 'Alumno'
