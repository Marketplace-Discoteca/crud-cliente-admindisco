from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    is_admindisco = models.BooleanField('admin disco', default=False)
    # is_customer = models.BooleanField('Is customer', default=False)
    # def __str__(self):
    #     return f"{self.id} - {self.username} - {self.email} - {self.is_superuser}"

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)

class Administrador(models.Model):
    id = models.AutoField(primary_key=True)

    # OPCIONES_DAR_DE_ALTA = [
    #     ('SI', 'Sí'),
    #     ('NO', 'No'),
    # ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre_discoteca = models.CharField(max_length=255)
    razon_social = models.CharField(max_length=255)
    ruc = models.CharField(max_length=11, unique=True)
    direccion = models.CharField(max_length=255)
    departamento = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    distrito = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo_personal = models.EmailField(blank=True, null=True)
    # dar_de_alta = models.CharField(max_length=2, choices=OPCIONES_DAR_DE_ALTA, default='NO')

    # def __str__(self):
    #     return f"{self.id} - {self.user.username} - {self.nombre_discoteca}"
