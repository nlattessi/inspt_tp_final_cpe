#from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
#from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import (Estado, Vendedor, CentroDistribucion,
                     Handheld, Incidente)
from .forms import (UserChangeForm, UserCreationForm)

from app.models import MyUser


class MyUserAdmin(UserAdmin):
    # The forms to add an change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in display the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User
    list_display = ('username', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')
         }),
    )
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()


class EstadoAdmin(admin.ModelAdmin):
    model = Estado
    list_display = ('nombre',)


class CentroDistribucionAdmin(admin.ModelAdmin):
    model = CentroDistribucion
    list_display = ('codigo', 'sucursal',)


class HandheldAdmin(admin.ModelAdmin):
    model = Handheld
    list_display = ('numero_de_serie', 'modelo', 'fecha_ultimo_cambio', 'estado', 'centro_distribucion',)


class VendedorAdmin(admin.ModelAdmin):
    model = Vendedor
    list_display = ('legajo', 'nombre', 'apellido', 'handheld')


class IncidenteAdmin(admin.ModelAdmin):
    model = Estado
    list_display = ('id', 'descripcion', 'solucion', 'handheld', 'vendedor', 'usuario')

# Now register the new UserAdmin...
admin.site.register(MyUser, MyUserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)

admin.site.register(Estado, EstadoAdmin)
admin.site.register(Vendedor, VendedorAdmin)
admin.site.register(CentroDistribucion, CentroDistribucionAdmin)
admin.site.register(Handheld, HandheldAdmin)
admin.site.register(Incidente, IncidenteAdmin)
