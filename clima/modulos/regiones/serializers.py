from rest_framework import serializers

from .models import paises, departamento

class paisesSerializers(serializers.ModelSerializer):
    class Meta:
        model = paises  
        fields = ('id', 'nombre_pais', 'sigla_pais',)