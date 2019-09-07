# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nflrcapp', '0013_auto_20190815_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prodev',
            name='thumbnail_desc',
            field=models.CharField(default='more...', max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='thumbnail_desc',
            field=models.CharField(default='more...', max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publication',
            name='thumbnail_desc',
            field=models.CharField(default='more...', max_length=500, null=True, help_text='140 characters or less. Appears on the item blocks.', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='storypage',
            name='thumbnail_desc',
            field=models.CharField(default='more...', max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
    ]
