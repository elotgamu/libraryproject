# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-06 03:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_auto_20171029_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='slug',
        ),
    ]
