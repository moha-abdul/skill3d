# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-25 11:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skillapp', '0011_auto_20181025_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Posts', to='skillapp.Profile'),
        ),
    ]
