from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView
from app.models import (Handheld, Vendedor, Incidente, CentroDistribucion,
                        HandheldCambioEstado)
from app.forms import (HandheldForm, HandheldCambiarEstadoForm,
                       HandheldCambiarCentroDistribucionForm,
                       HandheldCambiarVendedorForm, IncidenteCargarForm,
                       DispositivoCargarIncidenteForm)


def home(request):
    return render(request, 'home.html')

@login_required
def centros_distribucion(request):
    centros_distribucion = CentroDistribucion.objects.order_by('nombre')
    return render(request, 'centros_distribucion.html', {
        'centros_distribucion': centros_distribucion,
    })


@login_required
def handhelds(request):
    handhelds = Handheld.objects.order_by('fecha_ultimo_cambio')
    return render(request, 'handhelds.html', {
        'handhelds': handhelds,
    })


@login_required
def handheld(request, id):
    handheld = get_object_or_404(Handheld, pk=id)
    return render(request, 'handheld.html', {
        'handheld': handheld,
    })


@login_required
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


@login_required
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


@login_required
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


@login_required
def vendedores(request):
    vendedores = Vendedor.objects.order_by('legajo')
    return render(request, 'vendedores.html', {
        'vendedores': vendedores,
    })


@login_required
def vendedor(request, id):
    vendedor = get_object_or_404(Vendedor, pk=id)
    return render(request, 'vendedor.html', {
        'vendedor': vendedor,
    })


@login_required
def incidentes(request):
    incidentes = Incidente.objects.order_by('fecha_carga')
    return render(request, 'incidentes.html', {
        'incidentes': incidentes,
    })


@login_required
def incidente(request, id):
    incidente = Incidente.objects.get(id=id)
    incidente = get_object_or_404(Incidente, pk=id)
    return render(request, 'incidente.html', {
        'incidente': incidente,
    })


@login_required
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


# def login(request):
#     if request.method == 'POST':
#         usuario = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=usuario, password=password)
#         if user:
#             if user.is_active:
#                 auth_login(request, user)
#                 return redirect('home')
#             else:
#                 print ("Invalid login details: {0}, {1}".format(username, password))
#                 return HttpResponse("Tu cuenta esta desactivada.")
#         else:
#             return HttpResponse("Datos suministrados invalidos.")
#     return render(request, 'login.html')

    #     form = form_class(request.POST)
    #     print(form)
    #     print(form.is_valid())
    #     print(request.POST['username'])
    #     if form.is_valid():
    #         usuario = request.POST['username']
    #         password = request.POST['password']
    #         user = authenticate(username=usuario, password=password)
    #         print(usuario, password, user)
    #         if user:
    #             if user.is_active:
    #                 auth_login(request, user)
    #                 return redirect('home')
    #             else:
    #                 return HttpResponse("Tu cuenta esta desactivada.")
    #         else:
    #             print ("Invalid login details: {0}, {1}".format(username, password))
    #             return HttpResponse("Datos suministrados invalidos.")
    # else:
    #     form = form_class()
    # return render(request, 'login.html', {
    #     'form': form,
    # })

# @login_required
# def logout(request):
#     auth_logout(request)
#     return redirect('home')


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
