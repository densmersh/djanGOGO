# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-08 16:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0013_auto_20160308_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='public',
            name='date_pub',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 8, 19, 53, 47, 132232), verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='public',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]