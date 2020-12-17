# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2020-12-05 14:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_auto_20201204_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='achievements',
            field=models.TextField(blank=True, default='', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='clfy_bechalore',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='clfy_high_diplom',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='clfy_inter_diplom',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='clfy_master',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='clfy_other',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='clfy_phd',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='clfy_secondary',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='computer_knowledge',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='courses_1',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='courses_2',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='courses_3',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='courses_4',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='driving_license',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='driving_license_active',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='', max_length=20),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='email_other',
            field=models.EmailField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='experience',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='inq_accept_w_place',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='', max_length=200),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='inq_cust_contact',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No'), ('S', 'Sometimes')], default='', max_length=20),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='inq_explain',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='inq_favor_w_place',
            field=models.IntegerField(choices=[(1, 'Sanaa'), (2, 'Aden'), (3, 'IBB'), (4, 'Taiz'), (5, 'Thamar'), (6, 'Amran'), (7, 'Shabwa'), (8, 'Haja')], default='0'),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='inq_loan',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='', max_length=20),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='inq_long_term_disease',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='inq_surgery',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='inq_training',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No'), ('D', 'Not Now')], default='', max_length=20),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='inq_training_detail',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='internet_knowledge',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='job_favorite_hours',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='job_fit_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='job_in_bank_relat',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='job_know_channel',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='job_least_income',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='job_non_announcement',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='job_out_bank_relat',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='job_salary_exp',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='lang_ar',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='lang_en',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='lang_en_exam',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='lang_lang_exam',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='lang_other1',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='lang_other2',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='lang_toefl',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='skills',
            field=models.TextField(blank=True, default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='blood_type',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='close_contacts_1_Name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='close_contacts_1_job',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='close_contacts_1_phone',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='close_contacts_1_relation',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='close_contacts_1_residence_place',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='close_contacts_1_work_address',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='close_contacts_2_Name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='close_contacts_2_job',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='close_contacts_2_phone',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='close_contacts_2_relation',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='close_contacts_2_residence_place',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='close_contacts_2_work_address',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='email',
            field=models.EmailField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='home_phone',
            field=models.CharField(blank=True, default='0', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='residence_city',
            field=models.IntegerField(choices=[(1, 'Sanaa'), (2, 'Aden'), (3, 'IBB'), (4, 'Taiz'), (5, 'Thamar'), (6, 'Amran'), (7, 'Shabwa'), (8, 'Haja')], default='0'),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='residence_district',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='residence_place',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='residence_street',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='telegram',
            field=models.CharField(blank=True, default='0', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='whatsapp',
            field=models.CharField(blank=True, default='0', max_length=200, null=True),
        ),
    ]