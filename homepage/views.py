from django.forms import PasswordInput
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import RegistroForm, PaymentForm, PessoaForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Perfil, Pessoa
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import RegistroUtilizadorForm
from .forms import PerfilForm
# Create your views here.


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'home.html')
            else:
                return render(request, 'login.html', {'form': form})
        messages.error(request, 'Utilizador ou senha inválidos.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def home_view(request):
    return render(
        request, 
        'home.html',
        { 'logado':False, }
    )


def register_view(request):
    if request.method == 'POST':
        form = RegistroUtilizadorForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Conta criada para {username}! Agora você pode fazer login.')
            return render(request, 'login.html', {'form': form})
        else:
            messages.error(request,'Informações inválidas. Tente novamente.')
    else:
        form = RegistroUtilizadorForm()
    return render(request, 'register.html', {'form': form})

def password_recovery(request):
    return render(request, 'password_recovery.html')
    
def logout_view(request):
    logout(request)
    return render(request, 'home.html')  

def schedule_view(request):
    return render(request, 'schedule.html')


def payment_view(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redireciona para uma página de sucesso
    else:
        form = PaymentForm()
    return render(request, 'payment_form.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')

def obter_perfil(request, usuario_id):
    perfil = get_object_or_404(Perfil, usuario_id=usuario_id)
    dados = {
        'username': perfil.usuario.username,
        'email': perfil.usuario.email,
        'bio': perfil.bio,
        'telefone': perfil.telefone,
        'foto': perfil.foto.url if perfil.foto else '',
    }
    return JsonResponse(dados)


def obter_perfil(request, usuario_id):
    usuario = get_object_or_404(User, id=usuario_id)
    
    # Tente obter o perfil associado ao usuário (assumindo que você tenha um modelo Perfil)
    try:
        perfil = usuario.perfil  # Ajuste conforme o nome do seu modelo de perfil
        bio = perfil.bio if hasattr(perfil, 'bio') else ''
        telefone = perfil.telefone if hasattr(perfil, 'telefone') else ''
        foto = perfil.foto.url if hasattr(perfil, 'foto') and perfil.foto else ''
    except:
        bio = ''
        telefone = ''
        foto = ''
    
    dados = {
        'username': usuario.username,
        'email': usuario.email,
        'bio': bio,
        'telefone': telefone,
        'foto': foto,
    }
    return JsonResponse(dados)


def editar_pessoa(request, pessoa_id):
    pessoa = get_object_or_404(Pessoa, id=pessoa_id)
    if request.method == "POST":
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
    else:
        form = PessoaForm(instance=pessoa)

    return render(request, 'editar_pessoa.html', {'form': form})

@login_required
def perfil_view(request):
    
    perfil = Perfil.objects.get(username=request.user)
    
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = PerfilForm(instance=perfil)
    
    return render(request, 'perfil.html', {'form': form, 'perfil': perfil})

@login_required
def editar_perfil(request):
    user = request.user
    perfil = getattr(user, 'perfil', None) or Perfil(user=user)
    if request.method == 'POST':
        form = PerfilForm(request.POST, instance=perfil, user=user)
        if form.is_valid():
            form.save(user=user)
            return render(request, 'editar_perfil.html', {'form': form}) 
    else:
        form = PerfilForm(instance=perfil, user=user)
    return render(request, 'editar_perfil.html', {'form': form})

