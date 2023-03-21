from rest_framework import serializers

from .models import paises, departamento

class paisesSerializers(serializers.ModelSerializer):
    class Meta:
        model = paises  
        fields = ('id', 'nombre_pais', 'codigo_pais',)

class departamentoSerializers(serializers.ModelSerializer):
    class Meta:
        model = departamento  
        fields = ('id','pais', 'nombre_departamento', 'codigo_departamento',)