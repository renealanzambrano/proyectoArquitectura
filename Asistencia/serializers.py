# ----------------librerias------------
from rest_framework import routers, serializers, viewsets
from drf_dynamic_fields import DynamicFieldsMixin
# ----------------Modelos--------------
# Nombre app                      nombre modelo
from Asistencia.models import Asistencia

class AsistenciaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = ('__all__')