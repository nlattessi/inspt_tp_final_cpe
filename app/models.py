from datetime import datetime

from django.db import models
from django.utils import timezone
from django.conf import settings
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.contrib.contenttypes.models import ContentType


class AdminURLMixin(object):
    def get_admin_url(self):
        content_type = ContentType \
            .objects \
            .get_for_model(self.__class__)
        return reverse("admin:%s_%s_change" % (
            content_type.app_label,
            content_type.model),
            args=(self.id,))


class MyUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
        Creates and saves a User with the given username and password.
        """
        if not username:
            raise ValueError('Users must have an username.')

        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(username=username, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        # The user is identified by ther username
        return self.username

    def get_short_name(self):
        # The user is identified by ther username
        return self.username

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        # Does the user have a specific permission?
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        # Does the user have permissions to view the app 'app_label'?
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        # Is the user a member of staff?
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Estado(models.Model):
    nombre = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nombre


class Sucursal(models.Model):
    cuatro_numeros = RegexValidator(r'[0-9]{4}$', 'El codigo debe ser 4 numeros.')

    codigo = models.CharField(max_length=4, unique=True,
                              validators=[cuatro_numeros])
    nombre = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return "{}-{}".format(self.codigo, self.nombre)


class Handheld(models.Model):
    once_caracteres = RegexValidator(r'^[0-9a-zA-Z]{11}$',
                                     'Numero de serie debe de ser 11 caracteres alfanumericos.')

    numero_de_serie = models.CharField(max_length=11, unique=True,
                                       validators=[once_caracteres])
    modelo = models.CharField(max_length=255, blank=True)
    estado = models.ForeignKey(Estado)
    fecha_ultimo_cambio = models.DateTimeField(auto_now=True)
    sucursal = models.ForeignKey(
        Sucursal, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('handheld', kwargs={'pk': self.pk})

    def __str__(self):
        return self.numero_de_serie


class HandheldCambioEstado(models.Model):
    handheld = models.ForeignKey(Handheld)
    fecha_cambio = models.DateTimeField(auto_now=True)
    estado_anterior = models.ForeignKey(Estado,
        related_name='handheld_estadio_anterior'
    )
    nuevo_estado = models.ForeignKey(Estado,
        related_name='handheld_nuevo_estado'
    )
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


class Incidente(AdminURLMixin, models.Model):
    tipo = models.ForeignKey(TipoIncidente, related_name='tipo_incidente')
    descripcion = models.TextField()
    acciones = models.TextField(blank=True, null=True)
    handheld = models.ForeignKey(Handheld, blank=True, null=True)
    vendedor = models.ForeignKey(Vendedor, blank=True, null=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    fecha_carga = models.DateTimeField(default=timezone.now)
    revisado = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.id)
