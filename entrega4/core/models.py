from django.db import models

# Create your models here.
class datos(models.Model):
    rutcola = models.CharField(max_length=9, primary_key=True, verbose_name='Rut')
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    telefono = models.CharField(max_length=10, verbose_name='Telefono')
    direccion = models.CharField(max_length=30, verbose_name='Direccion')
    email = models.CharField(max_length=10, verbose_name='Email')
    pais = models.CharField(max_length=10, verbose_name='pais')
    contrasena = models.CharField(max_length=20, verbose_name='contrasena')
    
    def __str__(self):
        return self.nombre