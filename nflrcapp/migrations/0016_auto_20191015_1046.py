# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nflrcapp', '0015_homepagelevel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='thumbnail_desc',
            field=models.TextField(default='more ...', blank=True),
            preserve_default=True,
        ),
    ]
