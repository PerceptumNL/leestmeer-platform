# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 16:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20160418_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratedevent',
            name='max_rating',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='ratedevent',
            name='min_rating',
            field=models.IntegerField(default=0),
        ),
    ]
