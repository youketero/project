# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-16 19:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20170516_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='point2',
            name='Country',
            field=models.CharField(default=0, max_length=200),
        ),
    ]
