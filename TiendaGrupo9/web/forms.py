from django import forms
from django.core.exceptions import ValidationError
from .models import Vendedor
from django.contrib.auth.models import User
from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        exclude = ['vendedor', 'cliente']

class AltaProductosForms(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre_producto', 'descripcion', 'precio', 'imagen_url']
    
    def clean_nombre_producto(self):
        nombre = self.cleaned_data.get("nombre_producto")
        if not nombre.isalpha():
            raise forms.ValidationError("El nombre tiene que estar compuesto por letras")
        return nombre.upper()

    def clean_precio(self):        
        precio = self.cleaned_data["precio"]
        if precio <= 0:
            raise forms.ValidationError("El precio debe ser un número positivo")
        return precio

    def clean_descripcion(self):
        descripcion = self.cleaned_data["descripcion"]
        if not all(x.isalnum() or x.isspace() for x in descripcion):
            raise forms.ValidationError("La descripción tiene que estar compuesta por letras")
        return descripcion
    
    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get("nombre")
        
        if nombre and nombre.lower() == "teclado noga".lower():
            self.add_error('nombre', "El producto ya existe")

        return cleaned_data

class AltavendedorModelForm(forms.ModelForm):
    class Meta:
        model= Vendedor
        fields = '__all__'  

        error_messages = { #diccionario para almacenar mensajes de error, donde las claves serán los códigos de error y los valores serán los mensajes asociados a esos errores.
            'dni' :{
                'required' :'el campo dni es obligatorio :O'
            }
        }
    def clean_nombre(self):
        if not self.cleaned_data["nombre"].isalpha():
            raise ValidationError("El nombre tiene que estar compuesto por letras")

        self.cleaned_data["nombre"] = self.cleaned_data["nombre"].upper()

        return self.cleaned_data["nombre"]