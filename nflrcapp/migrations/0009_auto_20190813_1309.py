# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('nflrcapp', '0008_prodev_datestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prodev',
            name='datestamp',
            field=models.DateField(default=datetime.datetime(2019, 8, 13, 13, 9, 2, 731548)),
            preserve_default=True,
        ),
    ]
