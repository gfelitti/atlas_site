# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 20:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('councilman', '0005_auto_20170326_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='councilman',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='councilman.Councilman'),
        ),
    ]