from django.shortcuts import render
from .models import Formato, Marca, Categoria, Producto

def index(request):
    productos = Producto.objects.order_by('Nombre')
    return render(request, 'index.html', locals())