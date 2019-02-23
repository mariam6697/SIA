from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from datetime import date, datetime
from .models import TipoPago, Venta, Detalle
from .forms import VentaForm, DetalleForm, VentaFechaForm, VentaDayForm
import json

# Página principal de ventas
def index(request):
    ventas = Venta.objects.filter(Fecha__lte=datetime.now()).order_by('-Fecha')
    nompag = "Ventas"
    month = datetime.now().month
    if month == 1 or month == 3 or month == 4 or month == 7 or month == 8 or month == 10 or month == 12:
        dias = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
        numventas = []
        ingresos = []
        for dia in dias:
            count = 0
            ingr = 0
            for venta in ventas:
                if venta.Fecha.year == datetime.now().year and venta.Fecha.month == month and venta.Fecha.day == dia and venta.Estado == True:
                    ingr = ingr + venta.TotalAPagar
                    count = count + 1
            numventas.append(count)
            ingresos.append(ingr)
    elif month == 4 or month == 6 or month == 9 or month == 11:
        dias = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
        numventas = []
        ingresos = []
        for dia in dias:
            count = 0
            ingr = 0
            for venta in ventas:
                if venta.Fecha.year == datetime.now().year and venta.Fecha.month == month and venta.Fecha.day == dia and venta.Estado == True:
                    ingr = ingr + venta.TotalAPagar
                    count = count + 1
            numventas.append(count)
            ingresos.append(ingr)
    else:
        if datetime.now().year%4 == 0 and datetime.now().year%100 != 0 and datetime.now().year%400 == 0:
            dias = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
        elif datetime.now().year%4 != 0:
            dias = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
        numventas = []
        ingresos = []
        for dia in dias:
            count = 0
            ingr = 0
            for venta in ventas:
                if venta.Fecha.year == datetime.now().year and venta.Fecha.month == month and venta.Fecha.day == dia and venta.Estado == True:
                    ingr = ingr + venta.TotalAPagar
                    count = count + 1
            numventas.append(count)
            ingresos.append(ingr)
    dias = json.dumps(dias)
    numventas = json.dumps(numventas)
    return render(request, 'ventas/index.html', locals())

# Muestra una venta y sus detalles
def venta_detail(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    detalles = Detalle.objects.filter(NumeroVenta=venta.Codigo)
    idvent = json.dumps(venta.Codigo)
    nompag = "Venta N°"+str(venta.Codigo)
    if request.method == "POST":
        form = DetalleForm(request.POST)
        if form.is_valid():
            detalle = form.save(commit=False)
            detalle.NumeroVenta = Venta.objects.get(Codigo=pk)
            if detalle.Producto.Stock >= detalle.Cantidad:
                detalle.totald()
                detalle.save()
                return redirect('venta_detail', pk=detalle.NumeroVenta.Codigo)
            else:
                error = True
                producto = detalle.Producto
                stock = detalle.Producto.Stock
                form = DetalleForm()
    else:
        form = DetalleForm()
    venta.totalv()
    return render(request, 'ventas/venta_detail.html', locals())

# Confirma el pago de una venta y bloquea los botones de edición
def venta_pago(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    detalles = Detalle.objects.filter(NumeroVenta=venta.Codigo)
    venta.estado()
    for detalle in detalles:
        if detalle.Estado == False:
            detalle.stockd()
            detalle.Estado = True
            detalle.save()
    nompag = "Venta N°" + str(venta.Codigo)
    return render(request, 'ventas/venta_detail.html', locals())

# Crear una nueva venta
def venta_new(request):
    if request.method == "POST":
        form = VentaForm(request.POST)
        if form.is_valid():
            venta = form.save(commit=False)
            if request.user.first_name and request.user.last_name:
                venta.Vendedor = request.user.first_name + " " + request.user.last_name
            else:
                venta.Vendedor = request.user
            venta.save()
            return redirect('venta_detail', pk=venta.pk)
    else:
        form = VentaForm()
    nompag = "Añadir venta"
    return render(request, 'ventas/venta_edit.html', locals())

# Añadir un producto a una venta
def detalle_new(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == "POST":
        form = DetalleForm(request.POST)
        if form.is_valid():
            detalle = form.save(commit=False)
            detalle.NumeroVenta = Venta.objects.get(Codigo=pk)
            if detalle.Producto.Stock >= detalle.Cantidad:
                detalle.totald()
                detalle.save()
                return redirect('venta_detail', pk=detalle.NumeroVenta.Codigo)
            else:
                error = True
                producto = detalle.Producto
                stock = detalle.Producto.Stock
                form = DetalleForm()
    else:
        form = DetalleForm()
    nompag = "Añadir producto"
    return render(request, 'ventas/detalle_edit.html', locals())

# Editar un producto en venta (cambio de producto y/o cantidad)
def detalle_edit(request, pk):
    detalle = get_object_or_404(Detalle, pk=pk)
    if request.method == "POST":
        form = DetalleForm(request.POST, instance=detalle)
        if form.is_valid():
            detalle = form.save(commit=False)
            detalle.totald()
            detalle.save()
            return redirect('venta_detail', pk=detalle.NumeroVenta.Codigo)
    else:
        form = DetalleForm(instance=detalle)
    nompag = "Editar producto"
    return render(request, 'ventas/detalle_edit.html', locals())

# Editar venta
def venta_edit(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == "POST":
        form = VentaForm(request.POST, instance=venta)
        if form.is_valid():
            venta = form.save(commit=False)
            venta.save()
            return redirect('venta_detail', pk=venta.Codigo)
    else:
        form = VentaForm(instance=venta)
    nompag = "Editar venta"
    return render(request, 'ventas/venta_edit.html', locals())

# Eliminar un producto de una venta
def detalle_delete(request, pk):
    detalle = get_object_or_404(Detalle, pk=pk)
    if request.method == 'POST':
        prikey = detalle.NumeroVenta.Codigo
        detalle.delete()
        return redirect('venta_detail', pk=prikey)
    nompag = "Eliminar producto"
    return render(request, 'ventas/detalle_delete.html', locals())

# Elimina una venta
def venta_delete(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        venta.delete()
        return redirect('/ventas')
    nompag = "Eliminar venta"
    return render(request, 'ventas/venta_delete.html', locals())

# Todas las ventas
def ventas(request):
    ventas = Venta.objects.filter(Fecha__lte=date.today()).order_by('-Fecha')
    nompag = "Todas las ventas"
    return render(request, 'ventas/ventas.html', locals())

# Ventas por rango de fecha
def daterange(request):
    if request.method == "POST":
        form = VentaFechaForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['Fecha_inicial']
            end_date = form.cleaned_data['Fecha_final']
            ventas = Venta.objects.filter(Fecha__range=[start_date, end_date])
            if ventas:
                rec = 0
                for venta in ventas:
                    if venta.Estado:
                        rec = rec + venta.TotalAPagar
            else:
                error = True
                form = VentaFechaForm()
    else:
        form = VentaFechaForm()
    nompag = "Ventas por rango de fecha"
    return render(request, 'ventas/daterange.html', locals())

# Ventas por días
def ventas_day(request):
    hoy = date.today()
    if request.method == "POST":
        form = VentaDayForm(request.POST)
        if form.is_valid():
            fecha = form.cleaned_data['Fecha']
            ventas = Venta.objects.filter(Fecha=fecha)
            if ventas:
                rec = 0
                for venta in ventas:
                    if venta.Estado:
                        rec = rec + venta.TotalAPagar
            else:
                error = True
                form = VentaDayForm()
    else:
        form = VentaDayForm()
    nompag = "Ventas por día"
    return render(request, 'ventas/ventas_day.html', locals())

# Lista de meses
def ventas_month(request):
    ventas = Venta.objects.filter(Fecha__lte=datetime.now()).order_by('-Fecha')
    years = []
    for venta in ventas:
        if venta.Fecha.year not in years:
            years.append(venta.Fecha.year)
    months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    nompag = "Ventas por mes"
    return render(request, 'ventas/ventas_month.html', locals())

# Ventas por meses
def venta_month(request, year, month):
    ventas = Venta.objects.filter(Fecha__year=year, Fecha__month=month).order_by('-Fecha')
    year = year
    month = month
    rec = 0
    for venta in ventas:
        if venta.Estado:
            rec = rec + venta.TotalAPagar
    nompag = "Ventas por mes"
    if month == 1 or month == 3 or month == 4 or month == 7 or month == 8 or month == 10 or month == 12:
        dias = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
        numventas = []
        ingresos = []
        for dia in dias:
            count = 0
            ingr = 0
            for venta in ventas:
                if venta.Fecha.year == year and venta.Fecha.month == month and venta.Fecha.day == dia and venta.Estado == True:
                    ingr = ingr + venta.TotalAPagar
                    count = count + 1
            numventas.append(count)
            ingresos.append(ingr)
    elif month == 4 or month == 6 or month == 9 or month == 11:
        dias = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
        numventas = []
        ingresos = []
        for dia in dias:
            count = 0
            ingr = 0
            for venta in ventas:
                if venta.Fecha.year == date.today().year and venta.Fecha.month == month and venta.Fecha.day == dia and venta.Estado == True:
                    ingr = ingr + venta.TotalAPagar
                    count = count + 1
            numventas.append(count)
            ingresos.append(ingr)
    else:
        if venta.Fecha.year % 4 == 0 and venta.Fecha.year % 100 != 0 and venta.Fecha.year % 400 == 0:
            dias = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
        elif venta.Fecha.year % 4 != 0:
            dias = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
        numventas = []
        ingresos = []
        for dia in dias:
            count = 0
            ingr = 0
            for venta in ventas:
                if venta.Fecha.year == date.today().year and venta.Fecha.month == month and venta.Fecha.day == dia and venta.Estado == True:
                    ingr = ingr + venta.TotalAPagar
                    count = count + 1
            numventas.append(count)
            ingresos.append(ingr)
    dias = json.dumps(dias)
    numventas = json.dumps(numventas)
    return render(request, 'ventas/venta_month.html', locals())

# Lista de años
def ventas_year(request):
    ventas = Venta.objects.filter(Fecha__lte=datetime.now()).order_by('-Fecha')
    years = []
    for venta in ventas:
        if venta.Fecha.year not in years:
            years.append(venta.Fecha.year)
    nompag = "Ventas por año"
    return render(request, 'ventas/ventas_year.html', locals())

# Ventas por años
def venta_year(request, year):
    ventas = Venta.objects.filter(Fecha__year=year).order_by('-Fecha')
    months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    year = year
    rec = 0
    for venta in ventas:
        if venta.Estado:
            rec = rec + venta.TotalAPagar
    numventas = []
    ingresos = []
    for month in months:
        count = 0
        ingr = 0
        for venta in ventas:
            if venta.Fecha.year == year and venta.Fecha.month == month and venta.Estado == True:
                ingr = ingr + venta.TotalAPagar
                count = count + 1
        numventas.append(count)
        ingresos.append(ingr)
    nompag = "Ventas por año"
    numventas = json.dumps(numventas)
    return render(request, 'ventas/venta_year.html', locals())