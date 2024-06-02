from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name= "Nombre del Producto")
    descripcion = models.CharField(max_length=200, verbose_name= "Descripcion")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    imagen_url = models.URLField(verbose_name="Imagen")

class Cliente(models.Model):
    nombre = models.CharField(max_length=100, verbose_name= "Nombre del cliente")
    apellido = models.CharField(max_length=100, verbose_name= "Apellido del Cliente")
    dni = models.IntegerField(verbose_name="DNI del Cliente", unique=True)
    cliente_id = models.IntegerField(verbose_name="ID del cliente", unique=True)

class Vendedor(models.Model):
    nombre = models.CharField(max_length=100, verbose_name= "Nombre del Vendedor")
    apellido = models.CharField(max_length=100, verbose_name= "Apellido del Vendedor")
    vendedor_id = models.IntegerField(verbose_name="ID del Vendedor", unique=True)

class Pedido(models.Model):
    cliente_id = models.IntegerField(verbose_name="ID del cliente", unique=True)
    fecha_entrega = models.DateField(verbose_name="Fecha de Entrega")
    descripcion_pedido = models.CharField(max_length=200, verbose_name= "Descripcion")

 # MODELO DE DATOS 
"""
Producto
    nombre 
    descripcion
    precio
    imagen

Cliente 
    nombre 
    apellido
    dni

Vendedor 
    nombre
    apellido
    vendedor_id

Pedido
    cliente_id
    fecha_entrega 
    descripcion_pedido 
    
"""
