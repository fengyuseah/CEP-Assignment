# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0006_auto_20150713_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.CharField(default=b' ', max_length=3, null=True, choices=[(b'!!!', b'HIGH'), (b'!!', b'MEDIUM'), (b'!', b'LOW'), (b' ', b'------')]),
            preserve_default=True,
        ),
    ]
