# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nflrcapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prodev',
            name='title',
            field=models.CharField(max_length=200L, blank=True),
            preserve_default=True,
        ),
    ]
