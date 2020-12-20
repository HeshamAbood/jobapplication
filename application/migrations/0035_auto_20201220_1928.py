# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2020-12-20 16:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0034_auto_20201218_1617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobapp',
            name='ID_photo',
        ),
        migrations.RemoveField(
            model_name='jobapp',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='qualification',
            name='clfy_photo',
        ),
        migrations.AlterField(
            model_name='computerknowledge',
            name='computer_knowledge',
            field=models.CharField(blank=True, choices=[('Y', 'نعم'), ('N', 'لا')], default='', max_length=200, null=True, verbose_name='هل تستطيع استخدام الحاسب الآلي'),
        ),
        migrations.AlterField(
            model_name='computerknowledge',
            name='internet_knowledge',
            field=models.CharField(blank=True, choices=[('Y', 'نعم'), ('N', 'لا')], default='', max_length=200, null=True, verbose_name='هل تستطيع استخدام البريد الإلكتروني'),
        ),
        migrations.AlterField(
            model_name='drivinglicense',
            name='driving_license',
            field=models.CharField(choices=[('Y', 'نعم'), ('N', 'لا')], default='', max_length=200, null=True, verbose_name='هل تستطيع قيادة السيارات وسائل النقل'),
        ),
        migrations.AlterField(
            model_name='drivinglicense',
            name='driving_license_active',
            field=models.CharField(choices=[('Y', 'نعم'), ('N', 'لا')], default='', max_length=20, verbose_name='هل لديك رخصة قيادة سارية المفعول'),
        ),
        migrations.AlterField(
            model_name='inqueries',
            name='inq_accept_w_place',
            field=models.CharField(choices=[('Y', 'نعم'), ('N', 'لا')], default='', max_length=200, verbose_name='وهل تقبل العمل في محافظة إذا طلب منك ذلك'),
        ),
        migrations.AlterField(
            model_name='inqueries',
            name='inq_loan',
            field=models.CharField(choices=[('Y', 'نعم'), ('N', 'لا')], default='', max_length=20, verbose_name='هل عليك قروض أو ديون أو مشاكل مادية'),
        ),
        migrations.AlterField(
            model_name='jobapp',
            name='ID_type',
            field=models.CharField(choices=[('ID', 'بطاقة'), ('PS', 'جوازسفر'), ('O', 'أخرى')], max_length=200, verbose_name='نوع الهوية'),
        ),
        migrations.AlterField(
            model_name='jobapp',
            name='nationality',
            field=models.CharField(choices=[('Y', 'يمني'), ('O', 'أخرى')], max_length=200, verbose_name='الجنسية'),
        ),
        migrations.AlterField(
            model_name='jobapp',
            name='residence_city',
            field=models.IntegerField(choices=[(1, 'عمران'), (2, 'محافظة'), (3, 'الحديدة'), (4, 'الجوف'), (5, 'المحويت'), (6, 'أمانة'), (7, 'ذمار'), (8, 'حجة'), (9, 'إب'), (10, 'مأرب'), (11, 'محافظة'), (12, 'صعدة'), (13, 'صنعاء'), (14, 'تعز'), (15, 'عدن'), (16, 'أبين'), (17, 'محافظة'), (18, 'المهرة'), (19, 'حضرموت'), (20, 'أرخبيل'), (21, 'لحج'), (22, 'شبوة')], verbose_name='المحافظة'),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='inq_favor_w_place',
            field=models.IntegerField(choices=[(1, 'عمران'), (2, 'محافظة'), (3, 'الحديدة'), (4, 'الجوف'), (5, 'المحويت'), (6, 'أمانة'), (7, 'ذمار'), (8, 'حجة'), (9, 'إب'), (10, 'مأرب'), (11, 'محافظة'), (12, 'صعدة'), (13, 'صنعاء'), (14, 'تعز'), (15, 'عدن'), (16, 'أبين'), (17, 'محافظة'), (18, 'المهرة'), (19, 'حضرموت'), (20, 'أرخبيل'), (21, 'لحج'), (22, 'شبوة')], default='0'),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='residence_city',
            field=models.IntegerField(choices=[(1, 'عمران'), (2, 'محافظة'), (3, 'الحديدة'), (4, 'الجوف'), (5, 'المحويت'), (6, 'أمانة'), (7, 'ذمار'), (8, 'حجة'), (9, 'إب'), (10, 'مأرب'), (11, 'محافظة'), (12, 'صعدة'), (13, 'صنعاء'), (14, 'تعز'), (15, 'عدن'), (16, 'أبين'), (17, 'محافظة'), (18, 'المهرة'), (19, 'حضرموت'), (20, 'أرخبيل'), (21, 'لحج'), (22, 'شبوة')], default='0'),
        ),
        migrations.AlterField(
            model_name='lang',
            name='lang_type',
            field=models.CharField(choices=[('ar', 'العربية'), ('en', 'الإنجليزية'), ('o', 'اخرى')], default='', max_length=200, verbose_name='اللغة'),
        ),
        migrations.AlterField(
            model_name='langexam',
            name='lang_ex_type',
            field=models.CharField(choices=[('T', 'Toefel'), ('en', 'امتحان أخر باللغة الانجليزية'), ('o', 'امتحان أخر بلغة أخرى')], default='', max_length=200, null=True, verbose_name='هل سبق وتقدمت لامتحان اللغة'),
        ),
        migrations.AlterField(
            model_name='person',
            name='residence_city',
            field=models.CharField(choices=[(1, 'عمران'), (2, 'محافظة'), (3, 'الحديدة'), (4, 'الجوف'), (5, 'المحويت'), (6, 'أمانة'), (7, 'ذمار'), (8, 'حجة'), (9, 'إب'), (10, 'مأرب'), (11, 'محافظة'), (12, 'صعدة'), (13, 'صنعاء'), (14, 'تعز'), (15, 'عدن'), (16, 'أبين'), (17, 'محافظة'), (18, 'المهرة'), (19, 'حضرموت'), (20, 'أرخبيل'), (21, 'لحج'), (22, 'شبوة')], max_length=200),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='clfy_name',
            field=models.CharField(blank=True, choices=[('s', 'الثانوية'), ('id', 'دبلوم متوسط'), ('b', 'بكالوريوس'), ('hd', 'دبلوم عالي'), ('m', 'ماجيستير'), ('phd', 'دكتوراه'), ('o', 'اخرى')], default='', max_length=100, null=True, verbose_name='المؤهل الدراسي'),
        ),
    ]
