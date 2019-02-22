from django.contrib import admin
from .models import Formato, Marca, Categoria, Producto

class FormatoAdmin(admin.ModelAdmin):
    fields = ['Unidades', 'Descripcion',]
    list_display = ('Unidades', 'Descripcion',)

admin.site.register(Formato, FormatoAdmin)

class MarcaAdmin(admin.ModelAdmin):
    fields = ['Nombre',]
    list_display = ('Nombre',)

admin.site.register(Marca, MarcaAdmin)

class CategoriaAdmin(admin.ModelAdmin):
    fields = ['Nombre',]
    list_display = ('Nombre',)

admin.site.register(Categoria, CategoriaAdmin)

class ProductoAdmin(admin.ModelAdmin):
    fields = ['Codigo', 'Nombre', 'Marca', 'Categoria', 'Formato', 'Precio', 'Stock',]
    list_display = ('Codigo', 'Nombre', 'Marca', 'Categoria', 'Formato', 'Precio', 'Stock',)

admin.site.register(Producto, ProductoAdmin)