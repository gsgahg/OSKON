# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-13 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('o_nas', '0002_reference'),
    ]

    operations = [
        migrations.AddField(
            model_name='reference',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
