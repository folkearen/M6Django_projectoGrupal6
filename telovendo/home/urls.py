from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import *

app_name = 'home'
urlpatterns = [
    path('', bienvenida, name='bienvenida'),
    path('mostrarUsuario/', mostrarUsuario, name='mostrarUsuario'),
    path('contactanosProveedor', ingresarPosibleProveedor, name='contactanosProveedor'),
    path('signUp/', signUp, name='signUp'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/userAccount/', userAccount, name='userAccount'),
]