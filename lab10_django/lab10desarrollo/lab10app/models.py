from django.db import models

# Create your models here.

class Producto (models.Model):
    codigo = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=20)
    precio = models.CharField(max_length=20)
