# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-13 00:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='date',
            field=models.DateField(default=b'2016-11-13'),
        ),
    ]
