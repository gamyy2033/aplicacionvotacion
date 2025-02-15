# Generated by Django 5.1.5 on 2025-02-09 21:39

import Aplicaciones.Electoral.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Electoral', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votante',
            name='apellido',
            field=models.CharField(max_length=100, validators=[Aplicaciones.Electoral.models.validate_letters]),
        ),
        migrations.AlterField(
            model_name='votante',
            name='cedula',
            field=models.CharField(max_length=10, unique=True, validators=[Aplicaciones.Electoral.models.validate_cedula]),
        ),
        migrations.AlterField(
            model_name='votante',
            name='nombre',
            field=models.CharField(max_length=100, validators=[Aplicaciones.Electoral.models.validate_letters]),
        ),
    ]
