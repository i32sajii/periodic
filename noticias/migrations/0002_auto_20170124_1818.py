# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-24 18:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seccion',
            name='tipo',
            field=models.CharField(choices=[('P', 'Politicos'), ('M', 'Musicos'), ('A', 'Actores'), ('T', 'TecnoFauna'), ('C', 'Colaboradores')], max_length=100),
        ),
    ]
