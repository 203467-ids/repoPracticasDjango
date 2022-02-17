from re import A
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#importaciones de modelos agregados
from primerComponente.models import PrimerTabla

#importaciones de serializadores
from primerComponente.serializers import PrimerTablaSerializer

#import JSON
import json 

# Create your views here.
class PrimerTablaList(APIView):
  def res_custom(self,messages,pay_load, status):
    jsonRes = {"messages":messages,"pay_load":pay_load,"status":status}
    response = json.dumps(jsonRes)
    responseOk = json.loads(response)
    return responseOk
    
  def get(self, request, format=None):
    queryset=PrimerTabla.objects.all()
    serializer=PrimerTablaSerializer(queryset,many=True, context={'request':request})
    responseOk = self.res_custom("Success",serializer.data,status.HTTP_200_OK)
    return Response(responseOk)

  def post(self,request,format=None):
      serializer = PrimerTablaSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        datas = serializer.data
        return Response(self.res_custom("Success",datas, status.HTTP_201_CREATED))
      return Response(self.res_custom("Error", serializer.errors,status.HTTP_400_BAD_REQUEST))

class PrimerTablaDetail(APIView):
  def get_object(self,pk):
      try:
        return PrimerTabla.objects.get(pk = pk)
      except PrimerTabla.DoesNotExist:
        return "No existe"

  def get(self,request,pk,format=None):
    idResponse = self.get_object(pk)
    if idResponse != "No existe":
      idResponse = PrimerTablaSerializer(idResponse)
      return Response(idResponse.data,status=status.HTTP_200_OK)
    return Response(idResponse.errors, status = status.HTTP_400_BAD_REQUEST)

  def put(self,request,pk,format=None):
    idResponse = self.get_object(pk)
    serializer = PrimerTablaSerializer(idResponse, data=request.data)
    if serializer.is_valid():
      serializer.save()
      datas = serializer.data
      return Response(datas, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

  def delete(self, request,pk, format=None):
    idResponse = self.get_object(pk)
    if idResponse != "No existe":
      idResponse.delete()
      return Response("Dato eliminado", status = status.HTTP_201_CREATED)
    return Response("No existe",status = status.HTTP_400_BAD_REQUEST)
