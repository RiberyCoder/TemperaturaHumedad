import requests
from .models import paises
from .serializers import paisesSerializers


def generar_Peticion(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()

def get_temperaturas(pais):
    data = paises.objects.filter(sigla_pais=pais)
    serializer = paisesSerializers(data, many=True)
    
    response = generate_request('https://randomuser.me/api', params)
    if response:
       user = response.get('results')[0]
       return user.get('name').get('first')

    return ''"