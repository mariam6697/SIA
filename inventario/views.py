from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from .models import Producto, Proveedor, Pedido, IngresoProducto
from .forms import PedidoForm, IngresoForm, ProductoForm, FormatoForm, ProveedorForm
from django.http import HttpResponse

def index(request):
    nompag = 'Inventario'
    return render(request, 'inventario/index.html', locals())

# Lista de productos existentes
def productos(request):
    productos = Producto.objects.all()
    nompag = 'Productos'
    return render(request, 'inventario/productos.html', locals())

# Nuevo producto
def producto_new(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            nuevo = form.save(commit=False)
            nuevo.save()
            return redirect('productos')
    else:
        form = ProductoForm()
    nompag = "Productos nuevos"
    return render(request, 'inventario/producto_new.html', locals())

# Nuevo tipo de formato
def formato_new(request):
    if request.method == 'POST':
        form = FormatoForm(request.POST)
        if form.is_valid():
            nuevo = form.save(commit=False)
            nuevo.save()
            return redirect('productos')
    else:
        form = FormatoForm()
    nompag = "Nuevo formato"
    return render(request,'inventario/formato_new.html', locals())

# Productos por stock
def productos_stock(request):
    productos = Producto.objects.order_by('Stock')
    nompag = 'Stock de productos'
    return render(request, 'inventario/productos_stock.html', locals())

# Todos los pedidos
def pedidos(request):
    pedidos = Pedido.objects.filter(Fecha__lte=datetime.now()).order_by('-Fecha')
    nompag = 'Pedidos'
    return render(request, 'inventario/pedidos.html', locals())

# Ingresar nuevo pedido
def pedido_new(request):
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.Operador = request.user
            pedido.Fecha= datetime.now()
            pedido.save()
            return redirect('pedido_detail', pk=pedido.pk)
    else:
        form = PedidoForm()
    nompag = 'Ingresar pedido'
    return render(request, 'inventario/pedido_edit.html', locals())

# Editar pedido
def pedido_edit(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == "POST":
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.save()
            return redirect('pedido_detail', pk=pedido.Codigo)
    else:
        form = PedidoForm(instance=pedido)
    nompag = 'Editar pedido'
    return render(request, 'inventario/pedido_edit.html', locals())

# Muestra un pedido y los productos ingresados
def pedido_detail(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    ingresos = IngresoProducto.objects.filter(Pedido=pedido.Codigo)
    nompag = 'Pedido N° '+str(pedido.Codigo)
    return render(request, 'inventario/pedido_detail.html', locals())

# Confirma el ingreso y bloquea los botones de edición
def pedido_ingresado(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    ingresos = IngresoProducto.objects.filter(Pedido=pedido.Codigo)
    pedido.estado()
    for ingreso in ingresos:
        if ingreso.Estado == False:
            ingreso.Estado = True
            ingreso.save()
    nompag = 'Pedido N° ' + str(pedido.Codigo)
    return render(request, 'inventario/pedido_detail.html', locals())

# Elimina un pedido
def pedido_delete(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        pedido.delete()
        return redirect('pedidos')
    nompag = 'Eliminar pedido'
    return render(request, 'inventario/pedido_delete.html', locals())

# Eliminar producto del sistema
def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('productos')
    nompag = 'Eliminar producto'
    return render(request, 'inventario/producto_delete', locals())

# Editar producto
def producto_edit(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm (request.POST, instance=producto)
        if form.is_valid():
            producto = form.save(commit=False)
            form.save()
            return redirect('productos')
    else:
        form = ProductoForm()
    return render(request, 'inventario/producto_edit.html', locals())

# Añadir un ingreso de producto
def ingreso_new(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == "POST":
        form = IngresoForm(request.POST)
        if form.is_valid():
            ingreso = form.save(commit=False)
            ingreso.Pedido = Pedido.objects.get(Codigo=pk)
            ingreso.stockp()
            ingreso.save()
            return redirect('pedido_detail', pk=ingreso.Pedido.Codigo)
    else:
        form = IngresoForm()
    nompag = 'Ingresar producto'
    return render(request, 'inventario/ingreso_edit.html', locals())

# Editar un ingreso de producto (cambio de producto y/o cantidad)
def ingreso_edit(request, pk):
    ingreso = get_object_or_404(IngresoProducto, pk=pk)
    if request.method == "POST":
        form = IngresoForm(request.POST, instance=ingreso)
        if form.is_valid():
            ingreso = form.save(commit=False)
            ingreso.save()
            return redirect('ingreso_detail', pk=ingreso.Pedido.Codigo)
    else:
        form = IngresoForm(instance=ingreso)
    nompag = 'Editar ingreso'
    return render(request, 'inventario/ingreso_edit.html', locals())

# Eliminar un ingreso de producto
def ingreso_delete(request, pk):
    ingreso = get_object_or_404(IngresoProducto, pk=pk)
    if request.method == 'POST':
        prikey = ingreso.Pedido.Codigo
        ingreso.delete()
        return redirect('pedido_detail', pk=prikey)
    nompag = 'Eliminar ingreso'
    return render(request, 'inventario/ingreso_delete.html', locals())

# Ingresar un nuevo proveedor
def proveedor_new(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            prov = form.save(commit=False)
            prov.save()
            return redirect('productos')
    else:
        form = ProveedorForm()
    nompag = "Nuevo proveedor"
    return render(request, 'inventario/proveedor_new.html', locals())
