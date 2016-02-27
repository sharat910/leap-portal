# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0014_auto_20160226_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puser',
            name='contact',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
