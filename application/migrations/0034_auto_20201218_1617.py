# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2020-12-18 13:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0033_auto_20201216_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobdetails',
            name='job_salary_exp',
            field=models.CharField(default='', max_length=100, verbose_name='الراتب والمزايا المتوقعة'),
        ),
    ]