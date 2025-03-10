from django.urls import path
from . import views

urlpatterns = [
    path('', views.horario_semanal, name='horario_semanal'),
    path('aula/<int:aula_id>', views.reservar_aula, name='reservar_aula'),
    path('criar_aula/', views.criar_aula, name='criar_aula'),
]
