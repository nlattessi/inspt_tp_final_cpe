from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Estado(models.Model):
    nombre = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nombre


class CentroDistribucion(models.Model):
    nombre = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nombre


class Handheld(models.Model):
    numero_de_serie = models.CharField(max_length=255, unique=True)
    modelo = models.CharField(max_length=255, blank=True)
    marca = models.CharField(max_length=255, blank=True)
    fecha_ultimo_cambio = models.DateTimeField(auto_now=True)
    estado = models.ForeignKey(Estado)
    #vendedor = models.ForeignKey(Vendedor)
    centro_distribucion = models.ForeignKey(CentroDistribucion, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('handheld', kwargs={'pk': self.pk})

    def __str__(self):
        return self.numero_de_serie


class HandheldCambioEstado(models.Model):
    handheld = models.ForeignKey(Handheld)
    fecha_cambio = models.DateTimeField(auto_now=True)
    estado_anterior = models.ForeignKey(Estado, related_name='handheld_estadio_anterior')
    nuevo_estado = models.ForeignKey(Estado, related_name='handheld_nuevo_estado')

    def __str__(self):
        return "de {} a {} el {}".format(self.estado_anterior, self.nuevo_estado, self.fecha_cambio)


class Impresora(models.Model):
    numero_de_serie = models.CharField(max_length=255, unique=True)
    modelo = models.CharField(max_length=255, blank=True)
    marca = models.CharField(max_length=255, blank=True)
    fecha_ultimo_cambio = models.DateTimeField(auto_now=True)
    estado = models.ForeignKey(Estado)
    #vendedor = models.ForeignKey(Vendedor)
    centro_distribucion = models.ForeignKey(CentroDistribucion, blank=True, null=True)

    def __str__(self):
        return self.numero_de_serie


class ImpresoraCambioEstado(models.Model):
    impresora = models.ForeignKey(Impresora)
    fecha_cambio = models.DateTimeField(auto_now=True)
    estado_anterior = models.ForeignKey(Estado, related_name='impresora_estadio_anterior')
    nuevo_estado = models.ForeignKey(Estado, related_name='impresora_nuevo_estado')

    def __str__(self):
        return "de {} a {} el {}".format(self.estado_anterior, self.nuevo_estado, self.fecha_cambio)


class Vendedor(models.Model):
    legajo = models.CharField(max_length=255, unique=True)
    nombre = models.CharField(max_length=255, blank=True)
    apellido = models.CharField(max_length=255, blank=True)
    handheld = models.OneToOneField(Handheld, blank=True, null=True)
    impresora = models.OneToOneField(Impresora, blank=True, null=True)
    #centro_distribucion = models.ForeignKey(CentroDistribucion, blank=True, null=True)

    def __str__(self):
        return "{}, {} {}".format(self.legajo, self.nombre, self.apellido)


class Incidente(models.Model):
    descripcion = models.TextField()
    solucion = models.TextField()
    handheld = models.ForeignKey(Handheld, blank=True, null=True)
    impresora = models.ForeignKey(Impresora, blank=True, null=True)
    vendedor = models.ForeignKey(Vendedor, blank=True, null=True)
    usuario = models.ForeignKey(User, blank=True, null=True)
    fecha_carga = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.id)