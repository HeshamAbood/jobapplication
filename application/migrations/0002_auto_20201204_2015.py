# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2020-12-04 17:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='Hobbies',
            field=models.CharField(default='', max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='childs_number',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='close_contacts_1_Name',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='close_contacts_1_job',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='close_contacts_1_other_phone',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='close_contacts_1_phone',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='close_contacts_1_relation',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='close_contacts_1_residence_place',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='close_contacts_1_work_address',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='close_contacts_2_Name',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='close_contacts_2_job',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='close_contacts_2_other_phone',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='close_contacts_2_phone',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='close_contacts_2_relation',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='close_contacts_2_residence_place',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='close_contacts_2_work_address',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='home_phone',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='mobile_other',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='residence_city',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='residence_district',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='residence_place',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='residence_street',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='telegram',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='whatsapp',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
