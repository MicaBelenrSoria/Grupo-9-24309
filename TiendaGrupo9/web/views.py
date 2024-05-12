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
