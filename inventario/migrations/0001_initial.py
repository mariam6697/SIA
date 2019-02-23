# Generated by Django 2.1.7 on 2019-02-22 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('Codigo', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Formato',
            fields=[
                ('Codigo', models.AutoField(primary_key=True, serialize=False)),
                ('Unidades', models.CharField(max_length=50)),
                ('Descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('Codigo', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('Codigo', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
                ('Precio', models.IntegerField(default=0)),
                ('Stock', models.IntegerField(default=0)),
                ('Categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Categoria')),
                ('Formato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Formato')),
                ('Marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Marca')),
            ],
        ),
    ]