from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listado_productos', views.listado_productos, name='listado_productos'),
    path('listado_vendedores', views.VendedorListView.as_view(), name='listado_vendedores'),
    path('alta_productos', views.alta_productos, name='alta_productos'),
    path('alta_vendedor', views.alta_vendedor, name='alta_vendedor'),

]

