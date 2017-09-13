# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-13 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='description',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='link',
            name='title',
            field=models.CharField(max_length=40),
        ),
    ]