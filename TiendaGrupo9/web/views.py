from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect
from .models import Producto, Vendedor
from .forms import *
from django.views.generic.list import ListView
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime
from django.shortcuts import get_object_or_404
from .models import Producto
from .forms import AltaProductosForms
from .forms import ProductoForm

def index(request):

    # Accede a la base de datos atraves de los modelos 
    context = {
        # 'nombre': 'Comunidad Tecnológica', #Se le puede cambiar con el nombre ue ustedes quieren
        'fecha_hora': datetime.datetime.now() 
    }

    return render(request,'web/index.html', context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'web/login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request, 'Sesion terminada')
           
    return redirect('index')

@login_required
def listado_productos(request):
    productos = Producto.objects.all()
    contexto = {'productos': productos}
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



class VendedorListView(LoginRequiredMixin, ListView):
    model = Vendedor
    context_object_name= 'vendedores'
    template_name='web/listado_vendedores.html'
    ordening=['dni']

def alta_vendedor(request):
    context ={}

    if request.method == "GET":
        formulario = AltavendedorModelForm()
    else:
        formulario = AltavendedorModelForm(request.POST)

        if formulario.is_valid():

            formulario.save()
            

            messages.success(request, 'el vendedor fue dado de alta')

            return redirect('index')


    context ["formulario"] = formulario
    return render(request, 'web/alta_vendedor.html', context)

@login_required
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listado_productos')  # Redirige al listado de productos después de guardar
    else:
        form = ProductoForm(instance=producto)
    
    contexto = {'form': form, 'producto': producto}
    return render(request, 'web/editar_producto.html', contexto)  # Asegúrate que el nombre de la plantilla sea correcto

@login_required
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('listado_productos')  # Redirige al listado de productos después de eliminar
    
    contexto = {'producto': producto}
    return render(request, 'web/confirmar_eliminar.html', contexto)