from rest_framework import routers,serializers,viewsets

#Importacion de modelos
from primerComponente.models import PrimerTabla

class PrimerTablaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimerTabla
        fields = ('nombre', 'edad')
        #fields = ('pk','__all__')