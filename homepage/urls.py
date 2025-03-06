from django.urls import path
from .views import home_view
from django.contrib.auth import views as auth_views
from . import views

app_name='gym'

urlpatterns = [
    path('', home_view, name='home'),
    path('register/', views.register_view, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('schedule/', views.schedule_view, name='schedule'),
    #path('perfil/<int:usuario_id>/', views.obter_perfil, name='obter_perfil'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('perfil/', views.perfil_view, name='perfil_view'),
    path('editar-perfil/', views.editar_perfil, name='editar_perfil'),
    path('password-reset/', auth_views.PasswordResetView.as_view(
                                template_name='password_reset.html',
                                email_template_name='password_reset_email.html',
                                subject_template_name='password_reset_subject.txt',
                                success_url='/password-reset-done/'
                                ),
                            name='password_reset'),

    path('password-reset-done/', 
        auth_views.PasswordResetDoneView.as_view(
            template_name='password_reset_done.html')
        , name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(
             template_name='password_reset_confirm.html',
             success_url='/password-reset-complete/'
        ), 
        name='password_reset_confirm'),
    path('password-reset-complete/', 
        auth_views.PasswordResetCompleteView.as_view(
             template_name='password_reset_complete.html'
             ), 
        name='password_reset_complete'),
      
]    

