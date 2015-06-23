# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nflrcapp', '0002_auto_20141231_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='role',
            field=models.CharField(blank=True, max_length=30, null=True, choices=[('STAFF', 'NFLRC Staff'), ('ADVBOARD', 'Advisory Board'), ('COLLAB', 'Collaborator')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True, choices=[('DR', 'PhD.'), ('MR', 'Mr.'), ('MS', 'Ms.')]),
            preserve_default=True,
        ),
    ]
