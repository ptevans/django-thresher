# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-26 01:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0003_auto_20180226_0138'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='title',
            field=models.CharField(default='Worker', max_length=100),
            preserve_default=False,
        ),
    ]