# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 21:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chantiers', '0017_remove_message_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='chantier',
        ),
        migrations.AddField(
            model_name='chantier',
            name='messages',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='chantiers.Message'),
            preserve_default=False,
        ),
    ]
