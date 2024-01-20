from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=60, unique=True, null= False)
    password = models.CharField(max_length=10, unique=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null = False)

class Pedidos(models.Model):
    id_client = models.ForeignKey(Cliente, on_delete=models.CASCADE, null = False)
    descripcion = models.CharField(max_length=255, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null = False)
    created_at = models.DateTimeField(auto_now_add=True, null = False)
    