# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-13 17:08
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vyrobni_program', '0017_auto_20161013_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='long_description',
            field=ckeditor.fields.RichTextField(blank=True, max_length=5000, null=True),
        ),
    ]
