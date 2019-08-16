# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nflrcapp', '0012_auto_20190815_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prodev',
            name='date',
            field=models.CharField(help_text='specifies date range of event or other information.', max_length=50L, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='prodev',
            name='datestamp',
            field=models.DateField(help_text='this must strictly be a date in format yyyy-mm-dd'),
            preserve_default=True,
        ),
    ]
