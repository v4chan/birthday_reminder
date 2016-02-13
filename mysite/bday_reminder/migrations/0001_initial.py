# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-11 16:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('email', models.TextField()),
                ('phone', models.TextField()),
                ('birthday', models.DateField()),
                ('sent', models.BooleanField(default=False)),
            ],
        ),
    ]
