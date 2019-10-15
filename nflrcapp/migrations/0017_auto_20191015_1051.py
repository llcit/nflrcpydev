# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nflrcapp', '0016_auto_20191015_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prodev',
            name='thumbnail_desc',
            field=models.TextField(default='more ...', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publication',
            name='thumbnail_desc',
            field=models.TextField(default='more ...', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='storypage',
            name='thumbnail_desc',
            field=models.TextField(default='more ...', blank=True),
            preserve_default=True,
        ),
    ]
