# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-18 11:52
from __future__ import unicode_literals

from django.db import migrations
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20170611_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='place',
            field=location_field.models.plain.PlainLocationField(max_length=63, null=True),
        ),
    ]
