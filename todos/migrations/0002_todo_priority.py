# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='priority',
            field=models.CharField(default=b'L', max_length=1, choices=[(b'H', b'HIGH'), (b'M', b'MEDIUM'), (b'L', b'LOW')]),
            preserve_default=True,
        ),
    ]
