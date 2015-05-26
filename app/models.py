from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class Estado(models.Model):
    nombre = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nombre


class CentroDistribucion(models.Model):
    cuatro_numeros = RegexValidator(r'[0-9]{4}$', 'Codigo debe ser 4 numeros.')

    codigo = models.CharField(max_length=4, unique=True,
                              validators=[cuatro_numeros])
    sucursal = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return "{}-{}".format(self.codigo, self.sucursal)


class Handheld(models.Model):
    once_caracteres = RegexValidator(r'^[0-9a-zA-Z]{11}$',
                                     'Numero de serie debe de ser 11 caracteres alfanumericos.')

    numero_de_serie = models.CharField(max_length=11, unique=True,
                                       validators=[once_caracteres])
    modelo = models.CharField(max_length=255, blank=True)
    fecha_ultimo_cambio = models.DateTimeField(auto_now=True)
    estado = models.ForeignKey(Estado)
    centro_distribucion = models.ForeignKey(
        CentroDistribucion, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('handheld', kwargs={'pk': self.pk})

    def __str__(self):
        return self.numero_de_serie


class HandheldCambioEstado(models.Model):
    handheld = models.ForeignKey(Handheld)
    fecha_cambio = models.DateTimeField(auto_now=True)
    estado_anterior = models.ForeignKey(Estado,
                                        related_name='handheld_estadio_anterior')
    nuevo_estado = models.ForeignKey(
        Estado, related_name='handheld_nuevo_estado')
    observacion = models.TextField(blank=True)

    def __str__(self):
        return "de {} a {} el {}".format(self.estado_anterior, self.nuevo_estado, self.fecha_cambio)


class ModalidadVendedor(models.Model):
    nombre = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nombre


class Vendedor(models.Model):
    ocho_numeros = RegexValidator(r'^[0-9]{8}$', 'Legajo debe ser 8 numeros.')

    legajo = models.CharField(max_length=8, unique=True,
                              validators=[ocho_numeros])
    modalidad = models.ForeignKey(ModalidadVendedor, related_name='modalidad')
    nombre = models.CharField(max_length=255, blank=True)
    apellido = models.CharField(max_length=255, blank=True)
    handheld = models.OneToOneField(Handheld, blank=True, null=True)

    def __str__(self):
        return "{}, {} {}".format(self.legajo, self.nombre, self.apellido)


class TipoIncidente(models.Model):
    nombre = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nombre


class Incidente(models.Model):
    tipo = models.ForeignKey(TipoIncidente, related_name='tipo_incidente')
    descripcion = models.TextField()
    solucion = models.TextField()
    handheld = models.ForeignKey(Handheld, blank=True, null=True)
    vendedor = models.ForeignKey(Vendedor, blank=True, null=True)
    usuario = models.ForeignKey(User, blank=True, null=True)
    fecha_carga = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.id)
