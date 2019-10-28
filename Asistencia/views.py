#-----------------------LIBRERIAS-----------------------
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

#-----------------------MODELOS-------------------------
from Asistencia.models import Asistencia
#--------------------SERIALIZERS--------------------------
from Asistencia.serializers import AsistenciaSerializers

class AsistenciaList(APIView):
    def get(self, request, format=None):
        queryset = Asistencia.objects.all()
        serializer = AsistenciaSerializers(queryset, many=True, context = {'request':request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AsistenciaSerializers(data= request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response (datas)
        return Response(serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)

class AsistenciaDetail(APIView):
    # METODO CONSULTAR EL ID Y ME RETORNE SI EXISTE O NO
    def get_object(self, id):
        try:
            return Asistencia.objects.get(pk=id)
        except Asistencia.DoesNotExist:
            return "No"

    # METODO CONSULTAR EL ID Y DEVOLVER LOS VALORES DE SUS CAMPOS
    def get(self, request, id, format=None):
        asignature1 = self.get_object(id)
        serializer = AsistenciaSerializers(asignature1)
        return Response(serializer.data)
    
    # METODO CONSULTAR EL ID Y ACTULIZAR LOS VALORES DE SUS CAMPOS
    def put(self, request, id, format=None):
        asignature1 = self.get_object(id)
        serializer = AsistenciaSerializers(asignature1, data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #METODO DE ELIMINACION
    def delete(self, request, id, format=None):
        asignature1 = self.get_object(id)
        serializer = AsistenciaSerializers(asignature1, data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

