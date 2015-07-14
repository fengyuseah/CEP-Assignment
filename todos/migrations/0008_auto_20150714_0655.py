# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0007_auto_20150714_0654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.CharField(default=b' ', max_length=3, choices=[(b'!!!', b'HIGH'), (b'!!', b'MEDIUM'), (b'!', b'LOW'), (b' ', b'------')]),
            preserve_default=True,
        ),
    ]
