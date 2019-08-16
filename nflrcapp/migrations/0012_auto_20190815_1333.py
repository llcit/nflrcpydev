# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nflrcapp', '0011_auto_20190813_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prodev',
            name='datestamp',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
