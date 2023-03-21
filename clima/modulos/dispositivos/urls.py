from django.urls import path
from .views import *

urlpatterns = [
    path('api/getdispositivos/', DispositivosListView),
    path('api/getdispositivos/<str:codigo>', DispositivoListView),
]