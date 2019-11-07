#-----------------------LIBRERIAS-----------------------
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

#-----------------------MODELOS-------------------------
from registroRFID.models import Registro
#--------------------SERIALIZERS--------------------------
from registroRFID.serializers import RegistroSerializers

class RegistroList(APIView):
    def get(self, request, format=None):
        queryset = Registro.objects.all()
        serializer = RegistroSerializers(queryset, many=True, context = {'request':request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RegistroSerializers(data= request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data

            return Response (datas)
        return Response(serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)

class RegistroDetail(APIView):
    # METODO CONSULTAR EL ID Y ME RETORNE SI EXISTE O NO
    def get_object(self, id):
        try:
            return Registro.objects.get(pk=id)
        except Registro.DoesNotExist:
            return "No"

    # METODO CONSULTAR EL ID Y DEVOLVER LOS VALORES DE SUS CAMPOS
    def get(self, request, id, format=None):
        student = self.get_object(id)
        serializer = RegistroSerializers(student)
        return Response(serializer.data)
    
    # METODO CONSULTAR EL ID Y ACTULIZAR LOS VALORES DE SUS CAMPOS
    def put(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = RegistroSerializers(student, data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #METODO DE ELIMINACION
    def delete(self, request, pk, format=None):
        register = self.get_object(pk)
        register.delete()
        return Response('Eliminado correctamente')
