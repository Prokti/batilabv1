# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 16:44
from __future__ import unicode_literals

import chantiers.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chantiers', '0011_auto_20171023_0614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chantier',
            name='appel_1_doc',
            field=models.FileField(blank=True, upload_to=chantiers.models.renommage),
        ),
        migrations.AlterField(
            model_name='chantier',
            name='appel_2_doc',
            field=models.FileField(blank=True, upload_to=chantiers.models.renommage),
        ),
        migrations.AlterField(
            model_name='chantier',
            name='appel_3_doc',
            field=models.FileField(blank=True, upload_to=chantiers.models.renommage),
        ),
        migrations.AlterField(
            model_name='chantier',
            name='appel_4_doc',
            field=models.FileField(blank=True, upload_to=chantiers.models.renommage),
        ),
        migrations.AlterField(
            model_name='chantier',
            name='appel_5_doc',
            field=models.FileField(blank=True, upload_to=chantiers.models.renommage),
        ),
        migrations.AlterField(
            model_name='chantier',
            name='ccmi_doc',
            field=models.FileField(blank=True, upload_to=chantiers.models.renommage, verbose_name='CCMI'),
        ),
        migrations.AlterField(
            model_name='chantier',
            name='plans_os_doc',
            field=models.FileField(blank=True, upload_to=chantiers.models.renommage),
        ),
        migrations.AlterField(
            model_name='chantier',
            name='reception_doc',
            field=models.FileField(blank=True, upload_to=chantiers.models.renommage),
        ),
    ]
