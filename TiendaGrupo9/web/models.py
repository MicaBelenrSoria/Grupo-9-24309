from django.db import models

class Persona(models.Model):#clase para no repetir codigo(nom,ape,dni)
    nombre = models.CharField(max_length=100, verbose_name= "Nombre :")
    apellido = models.CharField(max_length=100, verbose_name= "Apellido :")
    dni = models.IntegerField(verbose_name="DNI :", unique=True)
    
    class Meta:
        abstract = True

class Cliente(Persona):
    cuil = models.IntegerField(verbose_name="cuil", unique=True, null=True)

class Vendedor(Persona):
    legajo = models.IntegerField(verbose_name="legajo", unique=True)

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=100, verbose_name= "nombre_producto")
    descripcion = models.CharField(max_length=200, verbose_name= "descripcion")
    precio = models.IntegerField(verbose_name="precio", unique=True)
    imagen_url = models.URLField(verbose_name="imagen_url")
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE, null=True, blank=True)
    # cliente: Relación ManyToMany con el modelo Cliente, lo que indica que múltiples clientes pueden comprar múltiples productos, y viceversa.
    cliente = models.ManyToManyField(Cliente , through = 'Pedido')

class Pedido(models.Model):
   
    fecha_entrega = models.DateField(verbose_name="Fecha de Entrega", auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto= models.ForeignKey(Producto, on_delete =models.CASCADE)

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
