# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-31 02:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20170330_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='user_like',
            field=models.ManyToManyField(blank=True, related_name='product_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
