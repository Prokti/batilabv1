# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-20 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chantiers', '0022_auto_20171107_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
