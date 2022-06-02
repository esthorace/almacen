from statistics import mode
from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()


class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.RESTRICT)
    producto = models.ForeignKey(Producto, on_delete=models.RESTRICT)
    fecha = models.DateField(auto_now=True)
    