# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nflrcapp', '0014_auto_20190904_1032'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('layer', models.IntegerField()),
                ('tag', models.ForeignKey(to='nflrcapp.ItemTag')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
