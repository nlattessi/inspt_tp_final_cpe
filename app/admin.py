from django.contrib import admin
from .models import (Estado, Vendedor, CentroDistribucion,
                     Handheld, Incidente)


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


admin.site.register(Estado, EstadoAdmin)
admin.site.register(Vendedor, VendedorAdmin)
admin.site.register(CentroDistribucion, CentroDistribucionAdmin)
admin.site.register(Handheld, HandheldAdmin)
admin.site.register(Incidente, IncidenteAdmin)
