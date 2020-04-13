from django.db import models
from datetime import datetime

class Formato(models.Model):
    Codigo = models.AutoField(primary_key=True)
    Unidades = models.CharField(max_length=50)
    Descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.Unidades+" "+self.Descripcion

class Marca(models.Model):
    Codigo = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre

class Categoria(models.Model):
    Codigo = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre

class Producto(models.Model):
    Codigo = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    Formato = models.ForeignKey(Formato, on_delete=models.CASCADE)
    Precio = models.IntegerField(default=0)
    Stock = models.IntegerField(default=0)
    Descripcion = models.TextField(max_length=500, default="Descripción del producto")

    def __str__(self):
        return self.Nombre+" "+self.Formato.Unidades+" "+self.Formato.Descripcion

class Proveedor(models.Model):
    Codigo = models.IntegerField(primary_key=True)
    Rut = models.IntegerField(default=0)
    Nombre = models.CharField(max_length=50)
    Telefono = models.IntegerField(default=0)

    def __str__(self):
        return (self.Nombre)

class Pedido(models.Model):
    Codigo = models.AutoField(primary_key=True)
    Proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    Fecha = models.DateTimeField(default=datetime.now, blank=True)
    Operador = models.CharField(max_length=50)
    Estado = models.BooleanField(default=False)

    def estado(self):
        self.Estado = True
        self.save()

    def __str__(self):
        return "N°"+str(self.Codigo)+' '+str(self.Fecha)

class IngresoProducto(models.Model):
    Codigo = models.AutoField(primary_key=True)
    Pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    Producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    Cantidad = models.IntegerField(default=0)
    Estado = models.BooleanField(default=False)

    def stockp(self):
        producto = self.Producto
        producto.Stock = producto.Stock + self.Cantidad
        producto.save()

    def __str__(self):
        return self.Producto.Nombre+' x' + self.Cantidad