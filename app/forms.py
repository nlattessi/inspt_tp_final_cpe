from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from .models import (MyUser, Handheld, Incidente, TipoIncidente)


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('username',)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match!")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        label=("Password"),
        help_text=("Raw passwords are not stored, so there is no way to see this user's password, but you can change the password using <a href=\"password/\">this form</a>.")
        )

    class Meta:
        model = MyUser
        fields = ('username', 'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]


class HandheldCambiarEstadoForm(forms.ModelForm):
    observacion = forms.CharField(required=False, widget=forms.Textarea)

    class Meta:
        model = Handheld
        fields = ('estado',)


class HandheldMoverSucursalForm(forms.ModelForm):
    class Meta:
        model = Handheld
        fields = ('sucursal',)


class VendedorCambiarHandheldForm(forms.Form):
    handheld = forms.ModelChoiceField(
        label="Asignar la handheld: ",
        queryset=Handheld.objects.filter(vendedor=None)
    )


class IncidenteCargarForm(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}),
        error_messages={'required': 'Este campo es requerido'},
    )
    acciones = forms.CharField(label='Acciones realizadas',
        widget=forms.Textarea(attrs={'rows': 3}),
        required=False,
    )

    class Meta:
        model = Incidente
        exclude = ['usuario', 'fecha_carga', 'revisado']
        error_messages = {
            'tipo': {
                'required': 'Este campo es requerido',
            },
        }


class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese  su nombre de usuario', 'class': 'form-control'}),
        error_messages={'required': 'Este campo es requerido'}
    )

    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Ingrese su password', 'class': 'form-control'}),
        required=True,
        error_messages={'required': 'Este campo es requerido'}
    )

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("El ingreso fue invalido. Por favor, vuelve a intentar.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user
