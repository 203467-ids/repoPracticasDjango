from rest_framework import serializers

#Importancion de modelos
from cargarImagen.models import ImagenTabla

class CargarImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenTabla
        fields = ('pk','name','format', 'url')
        