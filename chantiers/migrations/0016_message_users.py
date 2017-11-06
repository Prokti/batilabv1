# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 20:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chantiers', '0015_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
