from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventario/', include('inventario.urls')),
    path('ventas/', include('ventas.urls')),
    path('', LoginView.as_view(), name='login'),
    path('salir/', LogoutView.as_view(), name='logout'),
]