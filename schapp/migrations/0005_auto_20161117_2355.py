# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-17 23:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schapp', '0004_auto_20161117_2307'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='performance',
            options={'ordering': ('district_id',)},
        ),
        migrations.AlterModelOptions(
            name='school',
            options={'ordering': ('school_id',)},
        ),
    ]
