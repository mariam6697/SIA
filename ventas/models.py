from django.db import models
from datetime import date, datetime
from inventario.models import Producto

class TipoPago(models.Model):
    Codigo = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=50)

    def __str__(self):
        return (self.Nombre)

class Venta(models.Model):
    Codigo = models.AutoField(primary_key=True)
    Fecha = models.DateField(default=date.today(), blank=True)
    Hora = models.TimeField(default=datetime.now().time(), blank=True)
    TipoPago = models.ForeignKey(TipoPago, on_delete=models.CASCADE)
    Vendedor = models.CharField(max_length=50)
    TotalAPagar = models.IntegerField(default=0)
    Estado = models.BooleanField(default=False)

    def totalv(self):
        self.TotalAPagar = sum(Detalle.objects.values_list('TotalDetalle', flat=True).filter(NumeroVenta=self.Codigo))
        self.save()

    def estado(self):
        self.Estado = True
        self.save()

    def __str__(self):
        return "N°"+str(self.Codigo)+" "+str(self.Fecha)+" "+str(self.Hora)

class Detalle(models.Model):
    NumeroVenta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    Codigo = models.AutoField(primary_key=True)
    Producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    Cantidad = models.IntegerField(default=1)
    TotalDetalle = models.IntegerField(default=0)
    Estado = models.BooleanField(default=False)

    def totald(self):
        self.TotalDetalle = self.Cantidad*self.Producto.Precio
        self.save()

    def stockd(self):
        producto = self.Producto
        producto.Stock = producto.Stock - self.Cantidad
        producto.save()

    def __str__(self):
        return (self.Producto.Nombre+" "+self.Producto.Formato+" x "+str(self.Cantidad))
