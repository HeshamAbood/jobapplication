# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2020-12-05 17:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_auto_20201205_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='father_birth_place',
            field=models.CharField(max_length=200),
        ),
    ]
