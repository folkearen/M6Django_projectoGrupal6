from django.shortcuts import render, redirect
from .models import Usuario
from .forms import ProveedorForm, SignUp, LoginForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.decorators import *



# Create your views here.

def bienvenida(request):
    return render(request, 'home/index.html', {
        } )

def mostrarUsuario(request):
    lista_usuario = Usuario.objects.all()
    return render(request, 'home/mostrar_usuario.html', {
        'lista_usuario' : lista_usuario
    })

def ingresarPosibleProveedor(request):
    if request.method == 'POST':
        formulario = ProveedorForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('home:bienvenida')
    return render (request, 'home/proveedorPostulante.html',{'formulario' : ProveedorForm()})


def signUp(request):
    if request.method == 'POST':
        formulario_post = SignUp(request.POST)
        if formulario_post.is_valid():
            user = formulario_post.save(commit=False)
            user.save()
            login(request, user) 
            return redirect('home:userAccount')
    
    return render(request, 'home/signUp.html',{
        'form' : SignUp()
    })


class MyLoginView(LoginView):
    form_class =  LoginForm
    template_name = 'home/login.html'  


@login_required
def userAccount(request):
    return render(request, 'home/userAccount.html')
