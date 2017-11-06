# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-15 17:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chantiers', '0007_chantier_profil'),
    ]

    operations = [
        migrations.AddField(
            model_name='chantier',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
