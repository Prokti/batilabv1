# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-13 15:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0011_auto_20171113_1547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variante',
            name='groupe',
        ),
    ]
