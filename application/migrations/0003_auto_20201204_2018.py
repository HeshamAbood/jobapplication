# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2020-12-04 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_auto_20201204_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='blood_type',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')], max_length=200),
        ),
    ]
