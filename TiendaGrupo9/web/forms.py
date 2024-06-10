from django import forms
from django.core.exceptions import ValidationError

class AltaProductosForms(forms.Form):
    nombre = forms.CharField(max_length=100, label="Nombre", required=True)
    precio = forms.DecimalField(max_digits=10, decimal_places=2, label="Precio", required=True)
    descripcion = forms.CharField(widget=forms.Textarea, label="Descripcion", required=True)
    imagen_url = forms.URLField(label="Imagen del Producto")

    def clean_nombre(self):
        if not self.cleaned_data["nombre"].isalpha():
            raise ValidationError("El nombre tiene que estar compuesto por letras")

        self.cleaned_data["nombre"] = self.cleaned_data["nombre"].upper()

        return self.cleaned_data["nombre"]

    def clean_precio(self):        
        precio = self.cleaned_data["precio"]
        if precio <=0:
            raise ValidationError("El precio debe ser un número positivo")
        
        return precio

    def clean_descripcion(self):
        if not self.cleaned_data["descripcion"].isalpha():
            raise ValidationError("La descripcion tiene que estar compuesto por letras")

        return self.cleaned_data["descripcion"]
    
    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get("nombre")
        
        if nombre and nombre.lower() == "teclado noga".lower():
            self.add_error('nombre', "El producto ya existe")

        return cleaned_data