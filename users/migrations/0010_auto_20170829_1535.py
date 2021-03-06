# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-29 13:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_private_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='private_message',
            name='body',
            field=models.TextField(max_length=420),
        ),
        migrations.AlterField(
            model_name='private_message',
            name='recipient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipient', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='private_message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL),
        ),
    ]
