# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-11-16 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0008_transactsmodel_is_valid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactsmodel',
            name='tags',
            field=models.ManyToManyField(blank=True, to='trans.TagModel'),
        ),
    ]