# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-07 12:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chantiers', '0020_fichier'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fichier',
            old_name='fichier',
            new_name='fichier_path',
        ),
    ]
