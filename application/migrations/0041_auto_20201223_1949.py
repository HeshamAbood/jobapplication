# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2020-12-23 16:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0040_auto_20201223_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapp',
            name='residence_place',
            field=models.CharField(db_column=False, max_length=100, null=True, verbose_name='عنوان السكن الدائم'),
        ),
    ]
