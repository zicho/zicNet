# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-22 13:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0012_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='entry',
            new_name='belongs_to',
        ),
    ]
