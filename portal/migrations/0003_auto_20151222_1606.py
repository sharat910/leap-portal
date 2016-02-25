# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_auto_20151222_1606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='post_id',
        ),
        migrations.AddField(
            model_name='answer',
            name='query',
            field=models.ForeignKey(default=0, to='portal.Query'),
            preserve_default=False,
        ),
    ]
