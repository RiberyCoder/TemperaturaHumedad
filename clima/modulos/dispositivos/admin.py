from django.contrib import admin
from .models import dispositivos
# Register your models here.
@admin.register(dispositivos)
class dispositivosAdmin(admin.ModelAdmin):
    list_display=('codigo_dispositivo', 'nombre_dispositivo','tempmin_dispositivo','tempmax_dispositivo','modo_dispositivo', 'estadovent_dispositivo', 'fecha_registro')
    search_fields=('codigo_dispositivo', 'nombre_dispositivo','tempmin_dispositivo','tempmax_dispositivo','modo_dispositivo')