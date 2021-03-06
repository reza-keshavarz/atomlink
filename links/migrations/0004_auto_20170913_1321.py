# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-13 13:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0003_auto_20170913_1218'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('destination', models.CharField(max_length=300)),
                ('description', models.CharField(blank=True, max_length=140, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='link',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 13, 13, 21, 28, 433960, tzinfo=utc)),
        ),
    ]
