# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-14 14:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0015_auto_20160311_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='public',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='public',
            name='date_pub',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 14, 17, 11, 13, 403161), verbose_name='Дата публикации'),
        ),
    ]
