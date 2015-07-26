# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0009_auto_20150726_0031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='test',
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]
