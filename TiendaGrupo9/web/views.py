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
            'Teclado Noga',
            'Monitor Samsung',
            'Mouse Noga'
        ],

        'inventario_al_dia': True
    }

    return render(request, 'web/listado_productos.html', context)