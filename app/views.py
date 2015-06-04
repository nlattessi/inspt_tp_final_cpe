from functools import wraps
from datetime import datetime, timedelta, time
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from app.models import (Handheld, Vendedor, Incidente, Sucursal,
                        HandheldCambioEstado, Estado)
from app.forms import (HandheldCambiarEstadoForm,
                       HandheldMoverSucursalForm,
                       IncidenteCargarForm,
                       VendedorCambiarHandheldForm)


def login_and_admin(view_func):
    @login_required
    @user_passes_test(
        lambda u: u.is_admin,
        login_url='/denegado/',
        redirect_field_name=None)
    @wraps(view_func)
    def new_view_func(request, *args, **kwargs):
        response = view_func(request, *args, **kwargs)
        return response
    return new_view_func

class AdminRequiredMixin(object):
    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.is_admin,
        login_url='/denegado/', redirect_field_name=None))
    def dispatch(self, *args, **kwargs):
        return super(AdminRequiredMixin, self).dispatch(*args, **kwargs)


class HomeView(TemplateView):
    template_name = 'home.html'


@login_and_admin
def dashboard(request):
    estados = Estado.objects.all()
    sucursales = Sucursal.objects.order_by('nombre')
    total_handhelds = Handheld.objects.all().count()

    data = {}
    for sucursal in sucursales:
        data[sucursal] = {}
        for estado in estados:
            data[sucursal][estado] = 0
        for handheld in Handheld.objects.filter(sucursal=sucursal):
            data[sucursal][handheld.estado] += 1
    
    return render(request, 'dashboard.html', {
        'data': data,
        'estados': estados,
        'total_handhelds': total_handhelds,
    })


class IncidentesView(AdminRequiredMixin, ListView):
    model = Incidente
    template_name = "incidentes.html"
    context_object_name = 'incidentes'


class IncidentesDiaView(AdminRequiredMixin, ListView):
    model = Incidente
    template_name = "incidentes.html"
    context_object_name = "incidentes"

    def get_queryset(self):
        queryset = super(IncidentesDiaView, self).get_queryset()
        today = datetime.now().date()
        tomorrow = today + timedelta(1)
        today_start = datetime.combine(today, time())
        today_end = datetime.combine(tomorrow, time())
        return queryset.order_by('-fecha_carga').filter(fecha_carga__gte=today_start).filter(fecha_carga__lt=today_end)


@login_required
def cargar_incidente(request):
    form_class = IncidenteCargarForm
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            incidente = form.save(commit=False)
            incidente.user = request.user
            incidente.save()
            messages.success(request, 'Se cargo el incidente.')
            return redirect('home')
    else:
        form = form_class()
    return render(request, 'cargar_incidente.html', {
        'form': form,
    })


class HandheldBuscarView(AdminRequiredMixin, ListView):
    model = Handheld
    template_name = "handhelds.html"
    context_object_name = "handhelds"

    def get_queryset(self):
        queryset = super(HandheldBuscarView, self).get_queryset()
        q = self.request.GET.get("q")
        if q:
            return queryset.filter(numero_de_serie__icontains=q)
        return queryset.order_by('numero_de_serie')

@login_and_admin
def handheld_cambiar_estado(request, pk):
    handheld = get_object_or_404(Handheld, pk=pk)
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
            messages.success(request, 'Se cambio el estado a la handheld.')
            return redirect('home')
    else:
        form = form_class(instance=handheld)
    return render(request, 'handheld_cambiar_estado.html', {
        'handheld': handheld,
        'form': form,
    })


@login_and_admin
def handheld_mover_sucursal(request, pk):
    handheld = get_object_or_404(Handheld, pk=pk)
    form_class = HandheldMoverSucursalForm
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=handheld)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se movio la handheld de sucursal.')
            return redirect('home')
    else:
        form = form_class(instance=handheld)
    return render(request, 'handheld_mover_sucursal.html', {
        'handheld': handheld,
        'form': form,
    })


class VendedorBuscarView(AdminRequiredMixin, ListView):
    model = Vendedor
    template_name = "vendedores.html"
    context_object_name = "vendedores"

    def get_queryset(self):
        queryset = super(VendedorBuscarView, self).get_queryset()
        q = self.request.GET.get("q")
        if q:
            return queryset.filter(legajo__icontains=q)
        return queryset.order_by('legajo')


@login_and_admin
def vendedor_asignar_handheld(request, pk):
    vendedor = get_object_or_404(Vendedor, pk=pk)
    form_class = VendedorCambiarHandheldForm
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            nueva_handheld = form.cleaned_data['handheld']
            vendedor.handheld = nueva_handheld
            vendedor.save()
            messages.success(request, 'Se asigno la handheld al vendedor.')
            return redirect('home')
    else:
        form = form_class
    return render(request, 'vendedor_asignar_handheld.html', {
        'vendedor': vendedor,
        'form': form,
    })


@login_and_admin
def vendedor_remover_handheld(request, pk):
    vendedor = get_object_or_404(Vendedor, pk=pk)
    if request.method == 'POST':
        vendedor.handheld = None
        vendedor.save()
        messages.success(request, 'Se removio la handheld al vendedor.')
        return redirect ('home')
    else:
        return render(request, 'vendedor_remover_handheld.html', {
            'vendedor': vendedor,
        })


class ReportesView(AdminRequiredMixin, TemplateView):
    template_name = 'reportes.html'


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user:
                if user.is_active:
                    auth_login(request, user)
                    messages.success(request, 'Te logueaste con exito.')
                    if request.GET.get('next'):
                        return redirect(request.GET['next'])
                    else:
                        return redirect('home')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {
        'form': form,
    })


class DenegadoView(TemplateView):
    template_name = 'denegado.html'
