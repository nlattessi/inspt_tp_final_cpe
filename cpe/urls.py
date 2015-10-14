from django.conf.urls import include, url
from django.contrib import admin

from app import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls), name='admin'),

    url(r'^$', views.HomeView.as_view(), name='home'),

    url(r'^dashboard/$', views.dashboard, name='dashboard'),

    url(r'^incidentes/$', views.IncidenteView.as_view(), name='incidentes'),

    url(r'^incidentes_dia/$', views.IncidenteDiaView.as_view(),
        name='incidentes_dia'),

    url(r'^incidentes_sin_revisar/$',
        views.IncidenteSinRevisarView.as_view(),
        name='incidentes_sin_revisar'
    ),

    url(r'^incidentes_usuario/$',
        views.IncidenteUsuarioView.as_view(),
        name='incidentes_usuario'
    ),

    url(r'^incidentes/(?P<pk>[0-9]+)/$',
        views.IncidenteDetailView.as_view(),
        name='incidente_detail'
    ),

    url(r'^incidentes/revisar_incidente/(?P<pk>[0-9]+)/$',
        views.revisar_incidente,
        name='revisar_incidente'
    ),

    url(r'^incidentes/cargar_incidente/$', views.cargar_incidente,
        name='cargar_incidente'),

    url(r'^handhelds/buscar/$', views.HandheldBuscarView.as_view(),
        name='handheld_buscar'),

    url(r'^handhelds/(?P<pk>[0-9]+)/$',
        views.HandheldDetailView.as_view(),
        name='handheld_detail'
    ),

    url(r'^handhelds/(?P<pk>[0-9]+)/cambiar_estado/$',
        views.handheld_cambiar_estado,
        name='handheld_cambiar_estado'),

    url(r'^handhelds/(?P<pk>[0-9]+)/mover_sucursal$',
        views.handheld_mover_sucursal,
        name='handheld_mover_sucursal'),

    url(r'^vendedores/buscar/$', views.VendedorBuscarView.as_view(),
        name='vendedor_buscar'),

    url(r'^vendedores/(?P<pk>[0-9]+)/$',
        views.VendedorDetailView.as_view(),
        name='vendedor_detail'
    ),

    url(r'^vendedores/(?P<pk>[0-9]+)/asignar_handheld$',
        views.vendedor_asignar_handheld,
        name='vendedor_asignar_handheld'),

    url(r'^vendedores/(?P<pk>[0-9]+)/remover_handheld$',
        views.vendedor_remover_handheld,
        name='vendedor_remover_handheld'
    ),

    url(r'^accounts/login/$', views.login_view, name='login'),

    url(r'^accounts/logout/$', views.logout_view, name='logout'),

    url(r'^denegado/$', views.DenegadoView.as_view(), name='denegado'),
]
