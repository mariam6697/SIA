# Generated by Django 2.1.7 on 2019-02-22 21:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0003_auto_20190222_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='Hora',
            field=models.TimeField(blank=True, default=datetime.time(21, 58, 55, 885331)),
        ),
    ]
