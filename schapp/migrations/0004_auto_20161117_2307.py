# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-17 23:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schapp', '0003_auto_20161117_0557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performance',
            name='participation_rate_2014_to_2015',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='performance',
            name='percentage_meets_or_exceeds_2014_to_2015',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True),
        ),
    ]