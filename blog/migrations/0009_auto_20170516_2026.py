# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-16 17:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_viewsgeometrycolumns'),
    ]

    operations = [
        migrations.RenameField(
            model_name='point2',
            old_name='spatialReference',
            new_name='city',
        ),
    ]
