# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-25 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0002_auto_20170124_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seccion',
            name='tipo',
            field=models.CharField(choices=[('Politicos', 'Politicos'), ('Musicos', 'Musicos'), ('Actores', 'Actores'), ('TecnoFauna', 'TecnoFauna'), ('Colaboradores', 'Colaboradores')], max_length=100),
        ),
    ]
