# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 06:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Groupe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price_ht', models.FloatField()),
                ('code', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HouseAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HouseAttributePrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_ht', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='HouseAttributeValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('house_attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.HouseAttribute')),
            ],
        ),
        migrations.CreateModel(
            name='HouseItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.Groupe')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.House')),
                ('variantes', models.ManyToManyField(through='catalogue.HouseAttributePrice', to='catalogue.HouseAttributeValue')),
            ],
        ),
        migrations.AddField(
            model_name='houseattributeprice',
            name='house_attribute_value',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.HouseAttributeValue'),
        ),
        migrations.AddField(
            model_name='houseattributeprice',
            name='house_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.HouseItem'),
        ),
    ]
