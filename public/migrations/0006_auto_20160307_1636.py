# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-07 13:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0005_auto_20160307_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='public',
            name='author',
            field=models.CharField(default=0, max_length=100, verbose_name='Автор статьи'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='public',
            name='date_pub',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 7, 16, 36, 41, 431068), verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='public',
            name='text',
            field=models.TextField(max_length=10000, verbose_name='Текст публикации'),
        ),
    ]
