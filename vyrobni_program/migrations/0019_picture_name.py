# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-13 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vyrobni_program', '0018_auto_20161013_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True),
        ),
    ]
