# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-26 06:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skillapp', '0012_posts_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='profile',
        ),
        migrations.AddField(
            model_name='profile',
            name='posts',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='skillapp.Posts'),
        ),
    ]
