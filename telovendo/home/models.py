from django.db import models
from django.contrib.auth.models import AbstractUser, Group


class CustomGroup(Group):
    pass



      
class Usuario(AbstractUser):
  username = models.CharField(max_length=50, null=False, unique=True)
  nombre = models.CharField(max_length=50,  null=True)
  apellido = models.CharField(max_length=50,  null=True)
  rut = models.CharField(max_length=50,  null=True)
  email = models.EmailField(max_length=254,  null=True,  unique=True)
  telefono = models.CharField(max_length=15)
  fecha_registro = models.DateTimeField(auto_now=False, auto_now_add=True)
  password = models.CharField(max_length=128, null=True)
  
  def save(self, *args, **kwargs):
    self.username = self.email  # Asignamos el valor del email al username
    super().save(*args, **kwargs)



class UsuarioGroup(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    grupo = models.ForeignKey(CustomGroup, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['usuario', 'grupo']

class Proveedor(models.Model):
  nombre_empresa = models.CharField(max_length=200)
  nombre_solicitante = models.CharField(max_length=200)
  email = models.EmailField()
  telefono = models.CharField(max_length=15)
  rubro_proveedor = models.CharField(max_length=200)
  direccion = models.CharField(max_length=200)
  comentario = models.CharField(max_length=500)
  
  def __str__(self):
    return self.nombre_empresa + ' ' + self.nombre_solicitante


# Create your models here.



    #OJO Agregar los modelos al admin !!!


