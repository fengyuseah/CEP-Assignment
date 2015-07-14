# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0005_todo_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.CharField(default=b'L', max_length=3, choices=[(b'!!!', b'HIGH'), (b'!!', b'MEDIUM'), (b'!', b'LOW')]),
            preserve_default=True,
        ),
    ]
