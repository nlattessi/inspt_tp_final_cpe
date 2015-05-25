from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from app.models import (Handheld, Vendedor, Incidente, CentroDistribucion,
                        HandheldCambioEstado)
from app.forms import (HandheldForm, HandheldCambiarEstadoForm,
                       HandheldCambiarCentroDistribucionForm,
                       HandheldCambiarVendedorForm, IncidenteCargarForm,
                       DispositivoCargarIncidenteForm)


def home(request):
    return render(request, 'home.html')


def centros_distribucion(request):
    centros_distribucion = CentroDistribucion.objects.order_by('nombre')
    return render(request, 'centros_distribucion.html', {
        'centros_distribucion': centros_distribucion,
    })


def handhelds(request):
    handhelds = Handheld.objects.order_by('fecha_ultimo_cambio')
    return render(request, 'handhelds.html', {
        'handhelds': handhelds,
    })


def handheld(request, id):
    handheld = get_object_or_404(Handheld, pk=id)
    return render(request, 'handheld.html', {
        'handheld': handheld,
    })


def handheld_cambiar_estado(request, id):
    handheld = get_object_or_404(Handheld, pk=id)
    form_class = HandheldCambiarEstadoForm
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=handheld)
        if form.is_valid():
            estado_anterior = handheld.estado
            form.save()
            nuevo_registro_historico = HandheldCambioEstado()
            nuevo_registro_historico.handheld = handheld
            nuevo_registro_historico.estado_anterior = estado_anterior
            nuevo_registro_historico.nuevo_estado = form.cleaned_data['estado']
            nuevo_registro_historico.observacion = form.cleaned_data['observacion']
            nuevo_registro_historico.save()
            return redirect('handheld', id=handheld.id)
    else:
        form = form_class(instance=handheld)
    return render(request, 'handheld_cambiar_estado.html', {
        'handheld': handheld,
        'form': form,
    })


def handheld_cambiar_vendedor(request, id):
    handheld = get_object_or_404(Handheld, pk=id)
    vendedor_actual = Vendedor.objects.filter(handheld=handheld)
    form_class = HandheldCambiarVendedorForm
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            vendedor_nuevo = form.cleaned_data['vendedor']
            if vendedor_actual:
                vendedor_actual[0].handheld = None
                vendedor_actual[0].save()
            vendedor_nuevo.handheld = handheld
            vendedor_nuevo.save()
            return redirect('handheld', id=handheld.id)
    else:
        form = form_class
    return render(request, 'handheld_cambiar_vendedor.html', {
        'handheld': handheld,
        'form': form,
    })


def handheld_cargar_incidente(request, id):
    handheld = get_object_or_404(Handheld, pk=id)
    form_class = DispositivoCargarIncidenteForm
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            incidente = form.save(commit=False)
            incidente.user = request.user
            incidente.handheld = handheld
            incidente.save()
            return redirect('incidente', id=incidente.id)
    else:
        form = form_class()
    return render(request, 'handheld_cargar_incidente.html', {
        'form': form,
        'handheld': handheld,
    })

# def impresoras(request):
#     impresoras = Impresora.objects.order_by('fecha_ultimo_cambio')
#     return render(request, 'impresoras.html', {
#         'impresoras': impresoras,
#     })

# def impresora(request, id):
#     impresora = get_object_or_404(Impresora, pk=id)
#     return render(request, 'impresora.html', {
#         'impresora': impresora,
#     })

# def impresora_cambiar_estado(request, id):
#     impresora = get_object_or_404(Impresora, pk=id)
#     form_class = ImpresoraCambiarEstadoForm
#     if request.method == 'POST':
#         form = form_class(data=request.POST, instance=impresora)
#         if form.is_valid():
#             estado_anterior = impresora.estado
#             form.save()
#             nuevo_registro_historico = ImpresoraCambioEstado(
#                 impresora=impresora,
#                 estado_anterior=estado_anterior,
#                 nuevo_estado=form.cleaned_data['estado'])
#             nuevo_registro_historico.save()
#             return redirect('impresora', id=impresora.id)
#     else:
#         form = form_class(instance=impresora)
#     return render(request, 'impresora_cambiar_estado.html', {
#         'impresora': impresora,
#         'form': form,
#     })

# def impresora_cambiar_vendedor(request, id):
#     impresora = get_object_or_404(Impresora, pk=id)
#     vendedor_actual = Vendedor.objects.filter(impresora=impresora)
#     form_class = ImpresoraCambiarVendedorForm
#     if request.method == 'POST':
#         form = form_class(request.POST)
#         if form.is_valid():
#             vendedor_nuevo = form.cleaned_data['vendedor']
#             if vendedor_actual:
#                 vendedor_actual[0].impresora = None
#                 vendedor_actual[0].save()
#             if vendedor_nuevo:
#                 vendedor_nuevo.impresora = impresora
#                 vendedor_nuevo.save()
#             else:
#                 vendedor_actual[0].impresora = None
#                 vendedor_actual[0].save()
#             return redirect('impresora', id=impresora.id)
#     else:
#         form = form_class
#     return render(request, 'impresora_cambiar_vendedor.html', {
#         'impresora': impresora,
#         'form': form,
#     })

# def impresora_cargar_incidente(request, id):
#     impresora = get_object_or_404(Impresora, pk=id)
#     form_class = DispositivoCargarIncidenteForm
#     if request.method == 'POST':
#         form = form_class(request.POST)
#         if form.is_valid():
#             incidente = form.save(commit=False)
#             incidente.user = request.user
#             incidente.impresora = impresora
#             incidente.save()
#             return redirect('incidente', id=incidente.id)
#     else:
#         form = form_class()
#     return render(request, 'impresora_cargar_incidente.html', {
#         'form': form,
#         'impresora': impresora,
#     })


def vendedores(request):
    vendedores = Vendedor.objects.order_by('legajo')
    return render(request, 'vendedores.html', {
        'vendedores': vendedores,
    })


def vendedor(request, id):
    vendedor = get_object_or_404(Vendedor, pk=id)
    return render(request, 'vendedor.html', {
        'vendedor': vendedor,
    })


def incidentes(request):
    incidentes = Incidente.objects.order_by('fecha_carga')
    return render(request, 'incidentes.html', {
        'incidentes': incidentes,
    })


def incidente(request, id):
    incidente = Incidente.objects.get(id=id)
    incidente = get_object_or_404(Incidente, pk=id)
    return render(request, 'incidente.html', {
        'incidente': incidente,
    })


def cargar_incidente(request):
    form_class = IncidenteCargarForm
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            incidente = form.save(commit=False)
            incidente.user = request.user
            incidente.save()
            return redirect('incidente', id=incidente.id)
    else:
        form = form_class()
    return render(request, 'cargar_incidente.html', {
        'form': form,
    })


class HandheldListView(ListView):
    model = Handheld
    template_name = "handhelds.html"
    context_object_name = "handhelds"

    def get_queryset(self):
        queryset = super(HandheldListView, self).get_queryset()

        q = self.request.GET.get("q")
        if q:
            return queryset.filter(numero_de_serie__icontains=q)

        return queryset.order_by('fecha_ultimo_cambio')
