# Generated by Django 3.0.5 on 2020-04-14 23:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0007_auto_20200414_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='Hora',
            field=models.TimeField(blank=True, default=datetime.time(23, 4, 18, 990664)),
        ),
    ]
