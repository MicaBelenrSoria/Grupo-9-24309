from django import forms

class AltaProductosForms(forms.Form):
    nombre = forms.CharField(max_length=100, label="Nombre", required=True)
    precio = forms.DecimalField(max_digits=10, decimal_places=2, label="Precio", required=True)
    descripcion = forms.CharField(widget=forms.Textarea, label="Descripcion", required=True)
    imagen_url = forms.URLField(label="Imagen del Producto")

    
