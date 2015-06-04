from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from app import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls), name='admin'),

    url(r'^$', views.HomeView.as_view(), name='home'),

    url(r'^dashboard/$', views.dashboard, name='dashboard'),

    url(r'^incidentes/$', views.IncidentesView.as_view(), name='incidentes'),

    url(r'^incidentes_dia/$', views.IncidentesDiaView.as_view(),
        name='incidentes_dia'),

    url(r'^incidentes/cargar_incidente/$', views.cargar_incidente,
        name='cargar_incidente'),

    url(r'^handhelds/buscar/$', views.HandheldBuscarView.as_view(),
        name='handheld_buscar'),

    url(r'^handhelds/(?P<pk>[0-9]+)/cambiar_estado/$',
        views.handheld_cambiar_estado,
        name='handheld_cambiar_estado'),

    url(r'^handhelds/(?P<pk>[0-9]+)/mover_sucursal$',
        views.handheld_mover_sucursal,
        name='handheld_mover_sucursal'),

    url(r'^vendedores/buscar/$', views.VendedorBuscarView.as_view(),
        name='vendedor_buscar'),

    url(r'^vendedores/(?P<pk>[0-9]+)/asignar_handheld$',
        views.vendedor_asignar_handheld,
        name='vendedor_asignar_handheld'),

    url(r'^vendedores/(?P<pk>[0-9]+)/remover_handheld$',
        views.vendedor_remover_handheld,
        name='vendedor_remover_handheld'
    ),

    url(r'^reportes/$', views.ReportesView.as_view(), name='reportes'),

    url(r'^accounts/login/$', views.login_view, name='login'),

    url(r'^accounts/logout/$',
        'django.contrib.auth.views.logout',
        kwargs={'next_page': 'home'},
        name='logout',
    ),

    url(r'^denegado/$', views.DenegadoView.as_view(), name='denegado'),
]
