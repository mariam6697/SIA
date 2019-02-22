from django.db import models

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
    Codigo = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    Formato = models.ForeignKey(Formato, on_delete=models.CASCADE)
    Precio = models.IntegerField(default=0)
    Stock = models.IntegerField(default=0)

    def __str__(self):
        return self.Nombre+" "+self.Marca+" "+self.Formato