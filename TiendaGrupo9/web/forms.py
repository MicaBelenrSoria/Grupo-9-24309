from django import forms
from django.core.exceptions import ValidationError
class AltaProductosForms(forms.Form):
    nombre = forms.CharField(max_length=100, label="Nombre", required=True)
    precio = forms.DecimalField(max_digits=10, decimal_places=2, label="Precio", required=True)
    descripcion = forms.CharField(widget=forms.Textarea, label="Descripcion", required=True)
    imagen_url = forms.URLField(label="Imagen del Producto")

    def clean_nombre(self):
        if not self.cleaned_data["nombre"].isalpha():
            raise ValidationError("El nombre solo puede estar compuesto por letras")

        return self.cleaned_data["nombre"]
    
    def clean_precio(self):
        precio = self.cleaned_data["precio"]
        if not isinstance(precio, (int, float)):
            raise ValidationError("El precio solo puede estar compuesto por números")
        return precio
    
    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get("nombre")
        precio = cleaned_data.get("precio")
        
        # Ejemplo de validación combinada
        if nombre == "Producto" and precio == 0:
            raise ValidationError("El Producto no puede tener un precio de 0")
        
        return cleaned_data
