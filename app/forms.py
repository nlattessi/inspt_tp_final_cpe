from django import forms
from app.models import (Handheld, Vendedor, Incidente)


class HandheldForm(forms.ModelForm):
    class Meta:
        model = Handheld
        exclude = ['fecha_ultimo_cambio']


class HandheldCambiarEstadoForm(forms.ModelForm):
    observacion = forms.CharField(required=False, widget=forms.Textarea)
    class Meta:
        model = Handheld
        fields = ('estado',)


class HandheldCambiarCentroDistribucionForm(forms.ModelForm):
    class Meta:
        model = Handheld
        fields = ('centro_distribucion',)


class HandheldCambiarVendedorForm(forms.Form):
    vendedor = forms.ModelChoiceField(label="Asignar a: ",
                    queryset=Vendedor.objects.filter(handheld=None))


# class ImpresoraCambiarEstadoForm(forms.ModelForm):
#     class Meta:
#         model = Impresora
#         fields = ('estado',)


# class ImpresoraCambiarCentroDistribucionForm(forms.ModelForm):
#     class Meta:
#         model = Impresora
#         fields = ('estado',)


# class ImpresoraCambiarVendedorForm(forms.Form):
#     vendedor = forms.ModelChoiceField(label="Asignar a: ",
#                     queryset=Vendedor.objects.filter(impresora=None),
#                     required=False)


class IncidenteCargarForm(forms.ModelForm):
    class Meta:
        model = Incidente
        exclude = ['usuario', 'fecha_carga']


class DispositivoCargarIncidenteForm(forms.ModelForm):
    class Meta:
        model = Incidente
        exclude = ['usuario', 'handheld', 'fecha_carga']
