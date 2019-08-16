# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('nflrcapp', '0007_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='prodev',
            name='datestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 13, 12, 57, 21, 978262)),
            preserve_default=True,
        ),
    ]
