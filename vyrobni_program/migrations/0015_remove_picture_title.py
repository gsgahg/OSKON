# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-26 21:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vyrobni_program', '0014_picture_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='title',
        ),
    ]