# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 20:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chantiers', '0016_message_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='users',
        ),
    ]
