# Generated by Django 2.1.7 on 2019-02-22 03:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='Hora',
            field=models.TimeField(blank=True, default=datetime.time(3, 47, 56, 764633)),
        ),
    ]