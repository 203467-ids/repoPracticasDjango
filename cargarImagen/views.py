import datetime
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions
import os.path

#Importaciones de modelos
from cargarImagen.models import ImagenTabla

#Importacion de serializers
from cargarImagen.serializers import CargarImagenSerializer

class CargarImagenList(APIView):
    def get(self, request, format=None):
        queryset = ImagenTabla.objects.all()
        serializer = CargarImagenSerializer(queryset, many = True, context = {'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        if 'url' not in request.data:
            raise exceptions.ParseError(
                "No se selecciono ninguna imagen")
        files = request.data['url']
        name, formato = os.path.splitext(files.name)
        request.data['name'] = name
        request.data['format'] = formato
        serializer = CargarImagenSerializer(data = request.data)   
        if serializer.is_valid():
            validated_data = serializer.validated_data
            img = ImagenTabla(**validated_data)
            img.save()
            serializer_response = CargarImagenSerializer(img)
            return Response(serializer_response.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CargarImagenDetail(APIView):
    def get_object(self, pk):
        try:
            return ImagenTabla.objects.get(pk = pk)
        except ImagenTabla.DoesNotExist:
            return "No existe"

    def get(self, request,pk, format=None):
        idResponse = self.get_object(pk)
        if idResponse != "No existe":
            idResponse = CargarImagenSerializer(idResponse)
            return Response(idResponse.data, status = status.HTTP_200_OK)
        return Response("No hay datos", status = status.HTTP_400_BAD_REQUEST)
    
    
    def put(self, request,pk, format=None):
        idResponse = self.get_object(pk)
        files = request.data['url']
        name, formato = os.path.splitext(files.name)
        request.data['name'] = name
        request.data['format'] = formato
        serializer = CargarImagenSerializer(idResponse, data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas, status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        img = self.get_object(pk)
        if img != "No existe":
            img.url_img.delete(save=True)
            img.delete()
            return Response("Imagen eliminada",status=status.HTTP_204_NO_CONTENT)
        return Response("Imagen no encontrada",status = status.HTTP_400_BAD_REQUEST)
