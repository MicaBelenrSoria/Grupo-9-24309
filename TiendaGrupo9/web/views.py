from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect
from .models import Producto, Vendedor
from .forms import *
from django.views.generic.list import ListView
from django.contrib.auth import logout
import datetime

def index(request):

    # Accede a la base de datos atraves de los modelos 
    context = {
        # 'nombre': 'Comunidad Tecnológica', #Se le puede cambiar con el nombre ue ustedes quieren
        'fecha_hora': datetime.datetime.now() 
    }

    return render(request,'web/index.html', context)


def user_logout(request):
    logout(request)
    messages.success(request, 'Sesion terminada')
           
    return redirect('index')

def listado_productos(request):
    productos = Producto.objects.all() #.order_by("precio") es para filtrar lista segunprecio o lo que queramos

    contexto = {
        'productos': productos,  # Pasar el queryset de productos
        'producto_en_stock': True
    }

    return render(request, 'web/listado_productos.html', contexto)


def alta_productos(request):
    contexto = {}

    if request.method == "GET":
        contexto['alta_producto_form'] = AltaProductosForms()
    
    else: # Asumo que es un POST
        form = AltaProductosForms(request.POST)
        contexto['alta_producto_form'] = form

        # Validar el form
        if form.is_valid():
            # Si el form es correcto, lo redirijo a una vista segura por ejemplo index 
            # Si el form es incorrecto, se renderiza un form con mensajes de error  
            nuevo_producto = Producto(
                nombre_producto = form.cleaned_data['nombre_producto'],
                descripcion = form.cleaned_data['descripcion'],
                precio = form.cleaned_data['precio'],
                imagen_url = form.cleaned_data['imagen_url']
                )
            nuevo_producto.save()


            messages.success(request, 'el articulo fue dado de alta')
            return redirect('index')
    
    return render(request, 'web/alta_productos.html', contexto)


class VendedorListView(ListView):
    model = Vendedor
    context_object_name= 'vendedores'
    template_name='web/listado_vendedores.html'
    ordening=['dni']
def alta_vendedor(request):
    context ={}

    if request.method == "GET":
        formulario = AltaDocenteModelForm()
    else:
        formulario = AltaDocenteModelForm(request.POST)

        if formulario.is_valid():

            formulario.save()
            

            messages.success(request, 'el vendedor fue dado de alta')

            return redirect('index')


    context["formulario"] = formulario
    return render(request, 'web/alta_vendedor.html', context)
