from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name= "Nombre")
    descripcion = models.CharField(max_length=200, verbose_name= "Descripcion")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    imagen_url = models.URLField(verbose_name="Imagen")

 #Crear Migraciones 
 #python manage.py makemigrations web   

 #Ejecutar migracion