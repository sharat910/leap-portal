# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0011_alumni_media'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='description',
            field=models.TextField(default='a'),
            preserve_default=False,
        ),
    ]
