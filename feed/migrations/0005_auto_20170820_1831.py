# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-20 16:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0004_auto_20170820_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed_entry',
            name='publish_date',
            field=models.TimeField(default=b'2017-08-20 18:31:07'),
        ),
    ]
