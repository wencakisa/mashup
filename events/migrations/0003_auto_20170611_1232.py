# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-11 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20170610_1651'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='event',
            name='tickets_url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='photo',
            field=models.ImageField(upload_to='static/event_photos/'),
        ),
    ]
