# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-05 10:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0006_auto_20190505_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(max_length=64),
        ),
    ]
