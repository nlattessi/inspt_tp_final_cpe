from django.db import models
from django.contrib.auth.models import User


class Estado(models.Model):
    nombre = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nombre

class Vendedor(models.Model):
    legajo = models.CharField(max_length=255, unique=True)
    nombre = models.CharField(max_length=255, blank=True)
    apellido = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return "{}, {} {}".format(self.legajo, self.nombre, self.apellido)


class CentroDistribucion(models.Model):
    nombre = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nombre


class Handheld(models.Model):
    numero_de_serie = models.CharField(max_length=255, unique=True)
    modelo = models.CharField(max_length=255, blank=True)
    marca = models.CharField(max_length=255, blank=True)
    fecha_ultimo_cambio = models.DateTimeField(auto_now_add=True)
    estado = models.ForeignKey(Estado)
    vendedor = models.ForeignKey(Vendedor)
    centro_distribucion = models.ForeignKey(CentroDistribucion)

    def __str__(self):
        return self.numero_de_serie


class Impresora(models.Model):
    numero_de_serie = models.CharField(max_length=255, unique=True)
    modelo = models.CharField(max_length=255, blank=True)
    marca = models.CharField(max_length=255, blank=True)
    fecha_ultimo_cambio = models.DateTimeField(auto_now_add=True)
    estado = models.ForeignKey(Estado)
    vendedor = models.ForeignKey(Vendedor)
    centro_distribucion = models.ForeignKey(CentroDistribucion)

    def __str__(self):
        return self.numero_de_serie


class Incidente(models.Model):
    descripcion = models.TextField()
    solucion = models.TextField()
    handheld = models.ForeignKey(Handheld, blank=True, null=True)
    impresora = models.ForeignKey(Impresora, blank=True, null=True)
    vendedor = models.ForeignKey(Vendedor, blank=True, null=True)
    usuario = models.ForeignKey(User, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.id)