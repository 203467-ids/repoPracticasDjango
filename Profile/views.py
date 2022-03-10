# Create your views here.
from contextlib import nullcontext
from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions
import os
import datetime
#Importaciones de modelos
from Profile.models import Profile
from django.contrib.auth.models import User

import json 

#IMportacion de serializers
from Profile.serializers import ProfileSerializer

class ProfileTable(APIView):

    def get_objectUser(self, idUser):
        try:
            return User.objects.get(pk = idUser)#obtener id 
        except User.DoesNotExist:
            return "No existe"

    def post(self, request):
        idUser = request.data['id_user']
        userUpdate = request.data
        user = self.get_objectUser(idUser)
        if(user != "No existe"):
            dataRequest = request.data
            serializer = ProfileSerializer(data=dataRequest)
            if serializer.is_valid():
                validated_data = serializer.validated_data
                profile = Profile(**validated_data)
                profile.save()
                user = User.objects.filter(id=idUser)
                user.update(username=userUpdate.get('username'))
                user.update(first_name=userUpdate.get('first_name'))
                user.update(last_name=userUpdate.get('last_name'))
                user.update(email=userUpdate.get('email'))
                serializer_response = ProfileSerializer(profile)
                return Response(serializer_response.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Usuario no encontrado")
    
class ProfileTableDetail(APIView):
    def get_object(self, pk):
        try:
            return Profile.objects.get(id_user = pk)
        except Profile.DoesNotExist:
            return "No existe"

    def res_custom(self,user,data, status):
        jsonRes = {
            "first_name":user[0]['first_name'],
            "last_name":user[0]['last_name'],
            "username":user[0]['username'],
            "email":user[0]['email'],
            "id_user":data.get('id_user'),
            "url_img":data.get('url_img'),
            "status":status
        }
        response = json.dumps(jsonRes)
        responseOk = json.loads(response)
        return responseOk

    def get(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        user = User.objects.filter(id=pk).values()
        if idResponse != "No existe":
            idResponse = ProfileSerializer(idResponse)
            responseOk = self.res_custom(user,idResponse.data,status.HTTP_200_OK)
            return Response(responseOk)
        else:
            errorData = {
                "url_img" : "/assets/img-profile/default.jpg",
                "id_user" : pk
            }
        responseOk = self.res_custom(user,errorData,status.HTTP_400_BAD_REQUEST)
        return Response(responseOk)
    
    def put(self, request, pk, format=None):
        archivos = request.data['url_img']
        userUpdate = request.data
        idResponse = self.get_object(pk)
        if(idResponse != "No existe"):
            # actualizar datos del user
            user = User.objects.filter(id=pk)
            user.update(username=userUpdate.get('username'))
            user.update(first_name=userUpdate.get('first_name'))
            user.update(last_name=userUpdate.get('last_name'))
            user.update(email=userUpdate.get('email'))
            serializer = ProfileSerializer(idResponse)
            try:
                if(archivos == ""):
                    archivos = idResponse.url_img
                else:
                    os.remove('assets/'+str(idResponse.url_img))
            except os.error:
                print("La imagen no existe")
            idResponse.url_img = archivos
            idResponse.save()
            responseOk = self.res_custom(user.values(),serializer.data,status.HTTP_201_CREATED)
            return Response(responseOk)
        else:
            return Response("No hay registros")
    
    def delete(self, request, pk):
       
        profile = self.get_object(pk)
        if profile != "No existe":
            profile.url_img.delete(save=True)
            return Response("Imagen eliminada",status=status.HTTP_204_NO_CONTENT)
        return Response("Imagen no encontrada",status = status.HTTP_400_BAD_REQUEST)