# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-06 09:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rate',
            old_name='latest_rate',
            new_name='rate',
        ),
        migrations.RemoveField(
            model_name='provider',
            name='latest_rate',
        ),
        migrations.RemoveField(
            model_name='provider',
            name='latest_rate_updated_on',
        ),
        migrations.RemoveField(
            model_name='rate',
            name='api',
        ),
        migrations.RemoveField(
            model_name='rate',
            name='key',
        ),
        migrations.RemoveField(
            model_name='rate',
            name='latest_rate_updated_on',
        ),
        migrations.RemoveField(
            model_name='rate',
            name='name',
        ),
    ]
