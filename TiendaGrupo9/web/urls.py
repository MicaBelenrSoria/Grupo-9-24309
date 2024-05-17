from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listado_productos', views.listado_productos, name='listado_productos'),
    path('alta_productos', views.alta_productos, name='alta_productos'),
]

