# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-08-19 18:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='deposito',
            options={'ordering': ['nombre'], 'verbose_name_plural': 'Depositos'},
        ),
        migrations.AlterModelOptions(
            name='movimientoproducto',
            options={'ordering': ['producto'], 'verbose_name_plural': 'Movimiento Prod.'},
        ),
        migrations.AlterModelOptions(
            name='productodeposito',
            options={'ordering': ['deposito'], 'verbose_name_plural': 'Prod. x Depositos'},
        ),
    ]