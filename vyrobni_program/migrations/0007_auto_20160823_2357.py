# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-23 21:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vyrobni_program', '0006_auto_20160823_2354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='category',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
