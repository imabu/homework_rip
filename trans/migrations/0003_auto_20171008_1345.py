# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-10-08 10:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0002_auto_20171008_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactsmodel',
            name='created_dt',
            field=models.DateTimeField(verbose_name='Создано'),
        ),
    ]
