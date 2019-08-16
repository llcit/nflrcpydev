# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('nflrcapp', '0009_auto_20190813_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prodev',
            name='datestamp',
            field=models.DateField(default=datetime.datetime(2019, 8, 13, 13, 14, 31, 222476)),
            preserve_default=True,
        ),
    ]
