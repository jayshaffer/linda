# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-30 23:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tina', '0002_location_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='humidity',
            name='reading',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
        ),
        migrations.AddField(
            model_name='location',
            name='lat',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='location',
            name='long',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='temperature',
            name='reading',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
        ),
    ]
