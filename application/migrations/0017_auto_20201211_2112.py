# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2020-12-11 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0016_auto_20201211_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='residence_city',
            field=models.CharField(choices=[(1, 'Sanaa'), (2, 'Aden'), (3, 'IBB'), (4, 'Taiz'), (5, 'Thamar'), (6, 'Amran'), (7, 'Shabwa'), (8, 'Haja')], default='0', max_length=20),
        ),
    ]
