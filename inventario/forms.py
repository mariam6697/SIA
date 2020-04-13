from django import forms
from .models import Pedido, IngresoProducto, Producto, Formato, Proveedor

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ('Proveedor',)

class IngresoForm(forms.ModelForm):
    class Meta:
        model = IngresoProducto
        fields = ('Producto', 'Cantidad',)

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('Marca', 'Categoria', 'Formato', 'Nombre', 'Precio',)
        labels = {
            'Precio': 'Precio $',
        }

class FormatoForm(forms.ModelForm):
    class Meta:
        model = Formato
        fields = ('Unidades', 'Descripcion',)

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ('Rut','Nombre','Telefono',)
        labels = {
            'Telefono': 'Número telefónico',
        }