from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    codigo_recuperacao = models.CharField(max_length=6, blank=True, null=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def criar_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


class Dia(models.Model):
    data = models.DateField()
    dia_da_semana = models.CharField(max_length=10)

    def __str__(self):
        return self.dia_da_semana


class Horario(models.Model):
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()

    def __str__(self):
        return f"{self.hora_inicio} - {self.hora_fim}"


class Evento(models.Model):
    dia = models.ForeignKey(Dia, on_delete=models.CASCADE)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    evento = models.TextField(null=True, blank=True)
    instrutor_id = models.IntegerField(null=True, blank=True)
    sala_id = models.IntegerField(null=True, blank=True)
    tipo_aula_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.evento or "Evento"


class Payment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    card_number = models.CharField(max_length=16)
    expiry_date = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pagamento de {self.name}"  
    


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=None)
    email = models.CharField(max_length=200, null=False, blank=False)
    telemovel=models.CharField(max_length=20, null=True, blank=True)
    morada=models.CharField(max_length=100, null=True, blank=True)
    codigopostal=models.CharField(max_length=20, null=True, blank=True)
    cidade=models.CharField(max_length=20, null=True, blank=True)
    tipo = models.CharField(max_length=20, null=False, blank=False, default='0')
    dataregistro = models.DateTimeField(auto_now_add=True)
    

    
    def __str__(self):
        return self.username
    

from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    avaliacao = models.IntegerField(default=5)  # Estrelas de 1 a 5

    def __str__(self):
        return self.nome
