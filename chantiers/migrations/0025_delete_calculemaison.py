# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-21 05:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chantiers', '0024_fichier_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CalculeMaison',
        ),
    ]