# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nflrcapp', '0004_storypage_private'),
    ]

    operations = [
        migrations.AddField(
            model_name='prodev',
            name='listing_rank',
            field=models.IntegerField(default=0, help_text='default rank. higher the number, lower the rank', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='prodev',
            name='featured_rank',
            field=models.IntegerField(default=0, help_text='rank among other featured items. Higher the number, lower the rank', blank=True),
            preserve_default=True,
        ),
    ]
