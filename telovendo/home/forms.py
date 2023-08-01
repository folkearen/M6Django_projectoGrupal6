from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Proveedor, Usuario

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre_empresa','nombre_solicitante','email','telefono','rubro_proveedor','direccion','comentario']
        labels = {'Nombre empresa':'nombre_empresa',
                'Nombre solicitante' : 'nombre_solicitante',
                'Correo electrónico' : 'email',
                'Telefono de contacto' :'telefono',
                'Rubro de proveedor' :'rubro_proveedor',
                'Dirección' : 'direccion',
                'Comentario' : 'comentario'}

class SignUp(UserCreationForm):
    campos = (
        ('Administrador', 'admin'),
        ('Usuario comun', 'usuario_comun'),
        ('Moderador de permisos','permission_manger')
    )
    tipo_usuario = forms.ChoiceField(choices=campos)
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'rut', 'email', 'telefono', 'tipo_usuario']
        labels = {
            'Nombres': 'nombre',
            'Apellidos' : 'apellido',
            'Rut' : 'rut',
            'Correo electrónico' : 'email',
            'Teléfono' : 'telefono',
        }

class LoginForm(AuthenticationForm):
    username =forms.EmailField(max_length=254, widget=forms.TextInput(attrs={'class': 'login_input', 'placeholder': 'Ej: tunombre@example.com'}))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class': 'login_input', 'placeholder': '***********'}))
