# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-20 21:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chantiers', '0023_message_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='fichier',
            name='date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
