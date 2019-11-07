# ----------------librerias------------
from rest_framework import routers, serializers, viewsets
from drf_dynamic_fields import DynamicFieldsMixin
# ----------------Modelos--------------
# Nombre app                      nombre modelo
from rfidtemp.models import  rfidTemp

class rfidTempSerializers(DynamicFieldsMixin,serializers.ModelSerializer):
    class Meta:
        model = rfidTemp
        fields = ('__all__')
