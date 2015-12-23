# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_auto_20151222_1606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='enddate',
        ),
        migrations.RemoveField(
            model_name='event',
            name='startdate',
        ),
    ]
