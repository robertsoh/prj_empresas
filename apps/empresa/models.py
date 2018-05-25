from django.db import models


class TipoContribuyente(models.Model):
    codigo = models.CharField('RUC', max_length=6)
    nombre = models.CharField('Nombre', max_length=100)

    def __str__(self):
        return self.nombre


class Empresa(models.Model):
    ESTADO_ACTIVO = 'ACTIVO'
    ESTADO_INACTIVO = 'INACTIVO'
    ESTADO_CHOICES = (
        (ESTADO_ACTIVO, 'Activo'),
        (ESTADO_INACTIVO, 'Inactivo'),
    )
    CONDICION_HABIDO = 'HABIDO'
    CONDICION_NOHABIDO = 'NOHABIDO'
    CONDICION_CHOICES = (
        (CONDICION_HABIDO, 'Habido'),
        (CONDICION_NOHABIDO, 'No habido')
    )

    ruc = models.CharField('RUC', max_length=15)
    nombre = models.CharField('Nombre', max_length=150)
    tipo_contribuyente = models.ForeignKey(TipoContribuyente, verbose_name='Tipo contribuyente')
    nombre_comercial = models.CharField('Nombre comercial', max_length=150, blank=True, null=True)
    fecha_inscripcion = models.DateField('Fecha inscripción', blank=True, null=True)
    estado = models.CharField('Estado', max_length=10, choices=ESTADO_CHOICES, default=ESTADO_INACTIVO)
    condicion = models.CharField('Condición', max_length=10, choices=CONDICION_CHOICES, default= CONDICION_HABIDO)
    domicilio_fiscal = models.CharField('Domicilio fiscal', max_length=255, blank=True, null=True)

    def __str__(self):
        return '{} - {}'.format(self.ruc, self.nombre)
