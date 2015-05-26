from django import forms
from app.models import (Handheld, Vendedor, Incidente)


class HandheldForm(forms.ModelForm):
    class Meta:
        model = Handheld
        exclude = ['fecha_ultimo_cambio']


class HandheldFormAdmin(forms.ModelForm):
    numero_de_serie =forms.CharField(min_length=11, max_length=11)
    class Meta:
        model = Handheld
        fields = ('numero_de_serie',)


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


class IncidenteCargarForm(forms.ModelForm):
    class Meta:
        model = Incidente
        exclude = ['usuario', 'fecha_carga']


class DispositivoCargarIncidenteForm(forms.ModelForm):
    class Meta:
        model = Incidente
        exclude = ['usuario', 'handheld', 'fecha_carga']
