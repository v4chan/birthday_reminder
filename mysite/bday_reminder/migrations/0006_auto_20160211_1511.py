# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-11 20:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bday_reminder', '0005_auto_20160211_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_credential',
            name='expiry_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
