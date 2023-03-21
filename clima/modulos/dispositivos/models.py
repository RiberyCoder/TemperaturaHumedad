from django.db import models

    
class dispositivos(models.Model):

    nombre_dispositivo = models.CharField('Nombre del Dispositivo',max_length=100, blank=False, null=False)
    codigo_dispositivo = models.CharField('Codigo del Dispositivo', max_length=20, blank=False, null=False)
    modelo_dispositivo = models.CharField('Modelo del Dispositivo', max_length=20, blank=False, null=False)
    tempmin_dispositivo = models.IntegerField("Temperatura Minima", blank=False, null=False)
    tempmax_dispositivo = models.IntegerField("Temperatura Maxima", blank=False, null=False)
    modo_dispositivo = models.BooleanField("Modo Automatico", default=1)
    estadovent_dispositivo = models.BooleanField("Estado del Ventilador del dispositivo", default=1)
    fecha_registro = models.DateField("Fecha de Registro", auto_now=True)
    
    class Meta:
        verbose_name = "Dispositivo"
        verbose_name_plural = "Dispositivos"

    def __str__(self):
        return self.nombre_dispositivo
    
class vitacora(models.Model):
    
    dispositivo = models.ForeignKey('dispositivos', related_name='dispositivos', on_delete=models.PROTECT)
    nombre_dispositivo = models.CharField('Nombre del Dispositivo',max_length=100, blank=False, null=False)
    codigo_dispositivo = models.CharField('Codigo del Dispositivo', max_length=20, blank=False, null=False)
    modelo_dispositivo = models.CharField('Modelo del Dispositivo', max_length=20, blank=False, null=False)
    tempmin_dispositivo = models.IntegerField("Temperatura Minima", blank=False, null=False)
    tempmax_dispositivo = models.IntegerField("Temperatura Maxima", blank=False, null=False)
    modo_dispositivo = models.BooleanField("Modo Automatico", default=1)
    estadovent_dispositivo = models.BooleanField("Estado del Ventilador del dispositivo", default=1)
    fecha_registro = models.DateField("Fecha de Registro", auto_now=True)
    
    class Meta:
        verbose_name = "Dispositivo"
        verbose_name_plural = "Dispositivos"

    def __str__(self):
        return self.nombre_dispositivo
    
