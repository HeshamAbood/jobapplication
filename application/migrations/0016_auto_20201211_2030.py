# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2020-12-11 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0015_auto_20201211_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qualification',
            name='clfy_country',
            field=models.CharField(blank=True, default='', max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='clfy_place',
            field=models.CharField(blank=True, default='', max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='clfy_type',
            field=models.CharField(blank=True, default='', max_length=80, null=True),
        ),
    ]
