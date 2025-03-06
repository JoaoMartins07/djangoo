from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Payment, Pessoa  # Import the Payment model
from .models import Perfil

class RegistroForm(UserCreationForm):
    # Formulario de registro de usuario
    
    class Meta:
        model = User
        fields = ("username", "password", "password1")


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['name', 'email', 'card_number', 'expiry_date']


class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'avaliacao']

class RegistroUtilizadorForm(UserCreationForm):
    email = forms.CharField(max_length=200, required=True)
    telemovel = forms.CharField(max_length=15, required=False)
    
    class Meta:
        model = User
        fields = ['username', 'email','telemovel', 'password1', 'password2']



    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            Perfil.objects.create(
                user=user,
                email=self.cleaned_data['email']
            )
            perfil = super().save(commit=False)
            perfil.user = user
            if commit:
                perfil.save()
        return user
class PerfilForm(forms.ModelForm):
    email = forms.EmailField()
    email.label='Email'
    email.required=True
    
    first_name = forms.CharField()
    first_name.widget.attrs.update({'class': 'first_name'})
    last_name = forms.CharField()
    last_name.widget.attrs.update({'class': 'last_name'})

    class Meta:
        model = Perfil
        fields = ['email', 'telemovel', 'morada', 'codigopostal', 'cidade']
        
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['email'].initial = user.email
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name

    def save(self, user=None, commit=True):
        perfil = super().save(commit=False)
        if user:
            user.email = self.cleaned_data['email']
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            if commit:
                user.save()
                perfil.user = user
                perfil.save()
        return perfil
    


