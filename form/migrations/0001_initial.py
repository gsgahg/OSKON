# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-08 20:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=200, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('tel', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
