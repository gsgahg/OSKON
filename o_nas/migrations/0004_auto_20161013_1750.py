# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-13 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('o_nas', '0003_reference_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reference',
            name='link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
