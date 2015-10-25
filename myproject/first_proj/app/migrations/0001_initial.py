# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('date_time', models.TextField(null=True, blank=True, db_column='date & time')),
                ('use', models.FloatField(null=True, blank=True, db_column='use [kw]')),
            ],
            options={
                'managed': False,
                'db_table': 'better',
            },
        ),
    ]
