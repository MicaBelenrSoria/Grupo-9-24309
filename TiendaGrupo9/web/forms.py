from django import forms

class AltaProductosForms(forms.Form):
    nombre = forms.CharField(max_length=100)
    precio = forms.DecimalField(max_digits=10, decimal_places=2)
    descripcion = forms.CharField(widget=forms.Textarea)
    imagen_url = forms.URLField()
