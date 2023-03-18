from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import paisesSerializers
from .models import paises
from django.http import Http404
# Create your views here.
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