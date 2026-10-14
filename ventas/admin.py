from django.contrib import admin
from .models import cliente, pedido

admin.site.register(cliente)
class clienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'correo', 'ciudad')
    search_fields = ('nombre', 'apellido', 'correo')
    list_filter = ('ciudad',)
    
admin.site.register(pedido)
class pedidoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'producto', 'fecha', 'total', 'estado')
    search_fields = ('producto', 'cliente__nombre', 'cliente__apellido')
    list_filter = ('estado', 'fecha')
