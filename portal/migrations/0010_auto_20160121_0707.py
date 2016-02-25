# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0009_auto_20160121_0651'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Alumni',
        ),
        migrations.DeleteModel(
            name='Media',
        ),
    ]
