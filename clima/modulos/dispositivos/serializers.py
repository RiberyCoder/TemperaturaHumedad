from rest_framework import serializers

from .models import dispositivos

class dispositivoSerializers(serializers.ModelSerializer):
    class Meta:
        model = dispositivos  
        fields = ('id', 'nombre_dispositivo', 'codigo_dispositivo','modelo_dispositivo','tempmin_dispositivo','tempmax_dispositivo','modo_dispositivo','estadovent_dispositivo')
    