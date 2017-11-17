# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-13 11:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0008_housevariante_groupe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='variantes',
        ),
        migrations.RemoveField(
            model_name='housevariante',
            name='groupe',
        ),
        migrations.AddField(
            model_name='house',
            name='groupes',
            field=models.ManyToManyField(to='catalogue.Groupe'),
        ),
    ]
