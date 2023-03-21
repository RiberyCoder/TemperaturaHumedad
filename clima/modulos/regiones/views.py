from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from .response import SuccessRestResponse, ErrorRestResponse
from .serializers import paisesSerializers, departamentoSerializers
from .models import paises, departamento
from django.http import Http404
# Create your views here.
@api_view(['GET'])
def PaisesListView(request):
    try:
        data = paises.objects.order_by('id')
        serializer = paisesSerializers(data, many=True)
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
def CiudadesListView(request):
    try:
        data = departamento.objects.order_by('id')
        serializer = departamentoSerializers(data, many=True)
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
def CiudadListView(request, codigo):
    """
    Funcion que se encarga de listar todos los tipos de solicitudes a los difernetes
    sistemas y tipos de soporte
    :param request:
    :return:
    """
    try:
        data = departamento.objects.filter(pais=codigo).order_by('id')
        serializer = departamentoSerializers(data, many=True)
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
class paises_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        Paises = paises.objects.all()
        serializer = paisesSerializers(Paises, many=True)
        
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = paisesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class paises_APIView_Detail(APIView):
    def get_object(self, id):
        try:
            return paises.objects.get(pk=id)
        except paises.DoesNotExist:
            raise Http404
    def get(self, request, id, format=None):
        Pais = self.get_object(id)
        serializer = paisesSerializers(Pais)  
        return Response(serializer.data)