# Generated by Django 2.1.7 on 2019-02-22 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='Codigo',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]