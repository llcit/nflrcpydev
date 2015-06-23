# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nflrcapp', '0005_auto_20150622_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='listing_rank',
            field=models.IntegerField(default=0, help_text='default rank. higher the number, lower the rank', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='publication',
            name='listing_rank',
            field=models.IntegerField(default=0, help_text='default rank. higher the number, lower the rank', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='storypage',
            name='listing_rank',
            field=models.IntegerField(default=0, help_text='default rank. higher the number, lower the rank', blank=True),
            preserve_default=True,
        ),
    ]
