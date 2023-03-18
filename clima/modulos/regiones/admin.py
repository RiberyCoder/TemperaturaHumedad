from django.contrib import admin
from .models import paises, departamento

# Register your models here.
@admin.register(paises)
class paisesAdmin(admin.ModelAdmin):
    search_fields = ('nombre_pais',)
    
@admin.register(departamento)
class departamentoAdmin(admin.ModelAdmin):
    search_fields = ('nombre_departamento',)
    list_display = (
        'nombre_departamento',
        'codigo_departamento',
    )
