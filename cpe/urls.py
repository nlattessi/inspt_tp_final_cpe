from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView


from app import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.home, name='home'),

    url(r'^centros_distribucion/$', views.centros_distribucion,
        name='centros_distribucion'),

    url(r'^handhelds/$', views.handhelds, name='handhelds'),
    url(r'^handhelds/(?P<id>[0-9]+)/$', views.handheld, name='handheld'),
    url(r'^handhelds/(?P<id>[0-9]+)/cambiar_estado/$',
        views.handheld_cambiar_estado, name='handheld_cambiar_estado'),
    url(r'^handhelds/(?P<id>[0-9]+)/cambiar_vendedor/$',
        views.handheld_cambiar_vendedor, name='handheld_cambiar_vendedor'),
    url(r'^handhelds/(?P<id>[0-9]+)/cargar_incidente/$',
        views.handheld_cargar_incidente, name='handheld_cargar_incidente'),
    url(
        regex=r"^handhelds/buscar/$",
        view=views.HandheldListView.as_view(),
        name="handheld_buscar"
    ),

    # url(r'^impresoras/$', views.impresoras, name='impresoras'),
    # url(r'^impresoras/(?P<id>[0-9]+)/$', views.impresora, name='impresora'),
    # url(r'^impresoras/(?P<id>[0-9]+)/cambiar_estado/$',
    #     views.impresora_cambiar_estado, name='impresora_cambiar_estado'),
    # url(r'^impresoras/(?P<id>[0-9]+)/cambiar_vendedor/$',
    #     views.impresora_cambiar_vendedor, name='impresora_cambiar_vendedor'),
    # url(r'^impresoras/(?P<id>[0-9]+)/cargar_incidente/$',
    #     views.impresora_cargar_incidente, name='impresora_cargar_incidente'),

    url(r'^vendedores/$', views.vendedores, name='vendedores'),
    url(r'^vendedores/(?P<id>[0-9]+)/$', views.vendedor, name='vendedor'),

    url(r'^incidentes/$', views.incidentes, name='incidentes'),
    url(r'^incidentes/(?P<id>[0-9]+)/$', views.incidente, name='incidente'),
    url(r'^incidentes/cargar_incidente/$',
        views.cargar_incidente, name='cargar_incidente'),
]
