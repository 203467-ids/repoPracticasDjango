from django.urls import path, re_path
from django.conf.urls import include

#Importacion de vistas
from cargarImagen.views import CargarImagenList,CargarImagenDetail

urlpatterns = [
    re_path(r'^image/$', CargarImagenList.as_view()),
    re_path(r'^image/(?P<pk>\d+)$', CargarImagenDetail.as_view()),    
]