# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-20 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codebin', '0004_snippet_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='private',
            field=models.CharField(choices=[('PR', 'Private'), ('URL', 'Available by link'), ('PUB', 'Public')], default='PUB', max_length=3),
        ),
    ]
