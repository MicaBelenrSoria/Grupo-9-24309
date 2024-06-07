from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from .forms import *
from .models import Producto
import datetime

def index(request):

    # Accede a la base de datos atraves de los modelos 
    context = {
        'nombre': 'Comunidad Tecnológica', #Se le puede cambiar con el nombre ue ustedes quieren
        'fecha_hora': datetime.datetime.now() 
    }

    return render(request,'web/index.html', context)

def listado_productos(request):
    contexto = {
        'productos': [
            {
                'nombre': 'Teclado Noga',
                'descripcion': 'Un teclado ergonómico con retroiluminación LED.',
                'precio': 25.00,
                'imagen_url': 'web/img/teclado_noga.jpg',
            },
            {
                'nombre': 'Monitor Samsung',
                'descripcion': 'Monitor de 24 pulgadas con resolución Full HD.',
                'precio': 150.00,
                'imagen_url': 'web/img/monitor_samsung.webp',
            },
            {
                'nombre': 'Mouse Noga',
                'descripcion': 'Mouse óptico con sensor de alta precisión.',
                'precio': 15.000,
                'imagen_url': 'web/img/mouse_noga.jpeg',
            }
        ],
    }

    return render(request, 'web/listado_productos.html', contexto)

def alta_productos(request):
    contexto = {}

    if request.method == "GET":
        contexto['alta_producto_form'] = AltaProductosForms()
    
    else: # Asumo que es un POST
        form = AltaProductosForms(request.POST)
        contexto['alta_producto_form'] = form

        # Si el form es incorrecto, se renderiza un form con mensajes de error  

    return render(request, 'web/alta_productos.html', contexto)