# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2019-04-12 02:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190327_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='deny',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='job',
            name='approve',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='organization',
            name='approve',
            field=models.BooleanField(default=False),
        ),
    ]
