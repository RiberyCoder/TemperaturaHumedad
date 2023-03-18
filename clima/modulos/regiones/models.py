from django.db import models

# Create your models here.
class paises(models.Model):

    nombre_pais = models.CharField('Nombre del Pais',max_length=100, blank=False, null=False)
    sigla_pais = models.CharField('Sigla del Pais', max_length=2, blank=False, null=False)
    fecha_registro = models.DateField("Fecha de Registro", auto_now=True)
    class Meta:
        verbose_name = "Pais"
        verbose_name_plural = "Paises"

    def __str__(self):
        return self.nombre_pais
    
class departamento(models.Model):

    pais = models.ForeignKey('paises', related_name='Paiz', on_delete=models.PROTECT)
    nombre_departamento = models.CharField('Nombre del Departamento',max_length=100, blank=False, null=False)
    codigo_departamento = models.CharField('Codigo del Departamento', max_length=20, blank=False, null=False)
    fecha_registro = models.DateField("Fecha de Registro", auto_now=True)


    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"

    def __str__(self):
        return self.nombre_departamento
