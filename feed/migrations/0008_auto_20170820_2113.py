# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-20 19:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0007_auto_20170820_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed_entry',
            name='publish_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
