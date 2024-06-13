from django.contrib import admin
from .models import Cliente, Vendedor, Producto,Pedido
admin.site.register(Cliente)
admin.site.register(Vendedor)
admin.site.register(Producto)
admin.site.register(Pedido)
