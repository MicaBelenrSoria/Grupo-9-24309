from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listado_productos', views.listado_productos, name='listado_productos'),
]

