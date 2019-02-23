from django import forms
from datetime import date
from .models import Venta, Detalle

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ('TipoPago',)
        labels = {
            'TipoPago': 'Tipo de pago',
        }

class DetalleForm(forms.ModelForm):
    class Meta:
        model = Detalle
        fields = ('Producto', 'Cantidad',)

class VentaFechaForm(forms.Form):
    Fecha_inicial = forms.DateField(widget=forms.SelectDateWidget(years=range(1990, date.today().year+10)), initial=date.today())
    Fecha_final = forms.DateField(widget=forms.SelectDateWidget(years=range(1990, date.today().year+10)), initial=date.today())

class VentaDayForm(forms.Form):
    Fecha = forms.DateField(widget=forms.SelectDateWidget(years=range(1990, date.today().year+10)), initial=date.today())