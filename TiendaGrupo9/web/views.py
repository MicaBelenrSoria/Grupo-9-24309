from django.shortcuts import render
from django.http import HttpResponse
import datetime

def index(request):

    # Accede a la base de datos atraves de los modelos 
    context = {
        'nombre': 'Comunidad Tengnologica', #Se le puede cambiar con el nombre ue ustedes quieren
        'fecha_hora': datetime.datetime.now() 
    }

    return render(request,'web/index.html', context)

def listado_productos(request):
    context = {
        'productos': [
            {
                'nombre': 'Teclado Noga',
                'descripcion': 'Un teclado ergonómico con retroiluminación LED.',
                'precio': 25.00,
                'imagen_url': '.\web\static\web\img\teclado_noga.jpg'
            },
            {
                'nombre': 'Monitor Samsung',
                'descripcion': 'Monitor de 24 pulgadas con resolución Full HD.',
                'precio': 150.00,
                'imagen_url': '.\web\static\web\img\monitor_samsung.webp'
            },
            {
                'nombre': 'Mouse Noga',
                'descripcion': 'Mouse óptico con sensor de alta precisión.',
                'precio': 15.000,
                'imagen_url': '.\web\static\web\img\mouse_noga.jpeg'
            }
        ],

        'inventario_al_dia': True
    }

    return render(request, 'web/listado_productos.html', context)
