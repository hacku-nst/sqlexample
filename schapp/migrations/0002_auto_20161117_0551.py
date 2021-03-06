# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-17 05:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performance',
            name='district',
            field=models.CharField(default='', max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='performance',
            name='grade_level',
            field=models.CharField(default='', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='performance',
            name='school',
            field=models.CharField(default='', max_length=65, null=True),
        ),
        migrations.AlterField(
            model_name='performance',
            name='subgroup',
            field=models.CharField(default='', max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='performance',
            name='subject',
            field=models.CharField(default='', max_length=21, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='district',
            field=models.CharField(default='', max_length=46, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='school',
            field=models.CharField(default='', max_length=60, null=True),
        ),
    ]
