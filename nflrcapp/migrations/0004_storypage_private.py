# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nflrcapp', '0003_auto_20150325_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='storypage',
            name='private',
            field=models.BooleanField(default=False, help_text='checking this ON will require a user to login to view this story'),
            preserve_default=True,
        ),
    ]
