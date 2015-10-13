from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .models import (MyUser, Estado, Sucursal, Handheld, HandheldCambioEstado, ModalidadVendedor, Vendedor, TipoIncidente, Incidente)
from .forms import (UserChangeForm, UserCreationForm)


class MyUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('username', 'is_admin', 'is_active')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('is_admin', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')
         }),
    )
    search_fields = ['username']
    ordering = ('username',)
    filter_horizontal = ()


class EstadoAdmin(admin.ModelAdmin):
    model = Estado
    list_display = ('nombre',)
    search_fields = ['nombre']
    ordering = ('nombre',)


class SucursalAdmin(admin.ModelAdmin):
    model = Sucursal
    list_display = ('codigo', 'nombre',)
    search_fields = ['codigo', 'nombre']
    ordering = ('nombre',)


class HandheldAdmin(admin.ModelAdmin):
    model = Handheld
    list_display = ('numero_de_serie', 'modelo', 'fecha_ultimo_cambio', 'estado', 'sucursal',)
    search_fields = ['numero_de_serie', 'modelo', 'estado__nombre', 'sucursal__nombre']
    ordering = ('numero_de_serie',)
    list_filter = ('modelo', 'estado', 'sucursal',)


class HandheldCambioEstadoAdmin(admin.ModelAdmin):
    model = HandheldCambioEstado
    list_display = ('handheld', 'fecha_cambio', 'estado_anterior', 'nuevo_estado', 'observacion',)
    search_fields = ['handheld__numero_de_serie', 'estado_anterior__nombre', 'nuevo_estado__nombre', 'observacion']
    ordering = ('-fecha_cambio',)
    list_filter = ('estado_anterior', 'nuevo_estado',)


class ModalidadVendedorAdmin(admin.ModelAdmin):
    model = ModalidadVendedor
    list_display = ('nombre',)
    search_fields = ['nombre']
    ordering = ('nombre',)


class VendedorAdmin(admin.ModelAdmin):
    model = Vendedor
    list_display = ('legajo', 'nombre', 'apellido', 'handheld')
    search_fields = ['legajo', 'nombre', 'apellido', 'handheld']
    ordering = ('legajo',)


class TipoIncidenteAdmin(admin.ModelAdmin):
    model = Incidente
    list_display = ('nombre',)
    search_fields = ['nombre']
    ordering = ('nombre',)


class IncidenteAdmin(admin.ModelAdmin):
    model = Estado
    list_display = ('id', 'tipo', 'descripcion', 'acciones', 'handheld', 'vendedor', 'usuario', 'fecha_carga')
    search_fields = ['id', 'tipo__nombre', 'descripcion', 'solucion', 'handheld__numero_de_serie', 'vendedor__legajo', 'usuario__username']
    ordering = ('-fecha_carga',)
    list_filter = ('tipo', 'usuario',)


admin.site.register(MyUser, MyUserAdmin)
admin.site.unregister(Group)
admin.site.register(Estado, EstadoAdmin)
admin.site.register(Sucursal, SucursalAdmin)
admin.site.register(Handheld, HandheldAdmin)
admin.site.register(HandheldCambioEstado, HandheldCambioEstadoAdmin)
admin.site.register(ModalidadVendedor, ModalidadVendedorAdmin)
admin.site.register(Vendedor, VendedorAdmin)
admin.site.register(TipoIncidente, TipoIncidenteAdmin)
admin.site.register(Incidente, IncidenteAdmin)
