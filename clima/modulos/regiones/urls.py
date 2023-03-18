from django.urls import path
from .views import *

urlpatterns = [
    path('api/paises', paises_APIView.as_view()),
    path('api/paises/<int:id>/', paises_APIView_Detail.as_view()),
]