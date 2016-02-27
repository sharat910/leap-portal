# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0013_auto_20160203_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='achievements',
            field=models.TextField(null=True, blank=True),
        ),
    ]
