# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2020-12-04 18:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_auto_20201204_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='Hobbies',
            field=models.TextField(blank=True, default='', max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='ID_type',
            field=models.CharField(choices=[('ID', 'ID'), ('PS', 'Passport'), ('O', 'Other')], max_length=200),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='childs_number',
            field=models.CharField(blank=True, default=0, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='close_contacts_1_Name',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='close_contacts_1_job',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='close_contacts_1_other_phone',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='close_contacts_1_phone',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='close_contacts_1_relation',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='close_contacts_1_residence_place',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='close_contacts_1_work_address',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='close_contacts_2_Name',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='close_contacts_2_other_phone',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='close_contacts_2_phone',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='close_contacts_2_relation',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='close_contacts_2_residence_place',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='close_contacts_2_work_address',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='home_phone',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='mobile_other',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='residence_city',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='residence_district',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='residence_place',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='residence_street',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='telegram',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='whatsapp',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]