# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-24 14:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skillapp', '0006_section'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=100)),
                ('section', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Posts', to='skillapp.Section')),
            ],
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]