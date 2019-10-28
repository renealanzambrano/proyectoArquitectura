# ----------------librerias------------
from rest_framework import routers, serializers, viewsets
from drf_dynamic_fields import DynamicFieldsMixin
# ----------------Modelos--------------
# Nombre app                      nombre modelo
from registroRFID.models import Registro

class RegistroSerializers(DynamicFieldsMixin,serializers.ModelSerializer):
    class Meta:
        model = Registro
        fields = ('__all__')