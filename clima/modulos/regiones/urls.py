from django.urls import path
from .views import *

urlpatterns = [
    path('api/getpaises', PaisesListView, name='get_paises'),
    path('api/getdepartamentos', CiudadesListView, name='get_paises'),
    path('api/getdepartamentos/<str:codigo>', CiudadListView, name='solicitud_soporte_usuario'),

    path('api/paises', paises_APIView.as_view()),
    path('api/paises/<int:id>/', paises_APIView_Detail.as_view()),

]