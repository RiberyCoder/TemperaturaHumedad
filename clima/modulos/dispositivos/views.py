from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from .response import SuccessRestResponse, ErrorRestResponse
from .serializers import dispositivoSerializers
from .models import dispositivos
from django.http import Http404
# Create your views here.
@api_view(['GET'])
def DispositivosListView(request):
    try:
        data = dispositivos.objects.order_by('id')
        serializer = dispositivoSerializers(data, many=True)
        return SuccessRestResponse(
            message='Datos Solicitados de manera correcta',
            status=status.HTTP_202_ACCEPTED,
            data=serializer.data
        )
    except paises.DoesNotExist:
        return ErrorRestResponse(
            message='Datos no encontrados',
            status=status.HTTP_400_BAD_REQUEST
        )
        
@api_view(['GET'])
def DispositivoListView(request,codigo):
    try:
        data = dispositivos.objects.filter(codigo_dispositivo=codigo).order_by('id')
        serializer = dispositivoSerializers(data, many=True)
        return SuccessRestResponse(
            message='Datos Solicitados de manera correcta',
            status=status.HTTP_202_ACCEPTED,
            data=serializer.data
        )
    except dispositivos.DoesNotExist:
        return ErrorRestResponse(
            message='Datos no encontrados',
            status=status.HTTP_400_BAD_REQUEST
        )