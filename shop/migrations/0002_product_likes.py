# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-11 05:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
