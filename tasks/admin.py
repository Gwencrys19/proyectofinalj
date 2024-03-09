from django.contrib import admin
from .models import Productos,Categorias,Clientes,Ventas,Stock



class proAdmin(admin.ModelAdmin):
    readonly_fields =("fecha_de_creacion",) 

# Register your models here.
admin.site.register(Productos)
admin.site.register(Categorias,proAdmin)
admin.site.register(Clientes)
admin.site.register(Ventas)
admin.site.register(Stock)