# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('councilman', '0012_auto_20170401_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='councilman',
            name='status',
            field=models.IntegerField(choices=[(0, 'Inativo'), (1, 'Ativo')], default=1, verbose_name='Status'),
        ),
    ]
