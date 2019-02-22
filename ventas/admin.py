from django.contrib import admin
from .models import TipoPago, Venta, Detalle

class TipoPagoAdmin(admin.ModelAdmin):
    fields = ['Nombre',]
    list_display = ('Nombre',)

admin.site.register(TipoPago, TipoPagoAdmin)

class VentaAdmin(admin.ModelAdmin):
    fields = ['Fecha', 'Hora', 'TipoPago', 'Vendedor', 'TotalAPagar', 'Estado',]
    list_display = ('Fecha', 'Hora', 'TipoPago', 'Vendedor', 'TotalAPagar', 'Estado',)

admin.site.register(Venta, VentaAdmin)

class DetalleAdmin(admin.ModelAdmin):
    fields = ['NumeroVenta', 'Producto', 'Cantidad', 'TotalDetalle', 'Estado',]
    list_display = ('NumeroVenta', 'Producto', 'Cantidad', 'TotalDetalle', 'Estado',)

admin.site.register(Detalle, DetalleAdmin)