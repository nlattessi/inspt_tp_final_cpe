from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.forms import AuthenticationForm
from .models import (Handheld, Vendedor, Incidente)

from app.models import MyUser


class UserCreationForm(forms.ModelForm):
    """ A form for creating new users. Includes all the required fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('username',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match!")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField(label=("Password"),
        help_text=("Raw passwords are not stored, so there is no way to see this user's password, but you can change the password using <a href=\"password/\">this form</a>.")
        )

    class Meta:
        model = MyUser
        fields = ('username', 'is_active', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to initial value
        return self.initial["password"]


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


class LoginForm(AuthenticationForm):
    username = forms.CharField(label=("Username"),
                               max_length=30,
                               widget=forms.TextInput(attrs={'class': 'loginput'}))
