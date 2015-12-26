# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_event_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='puser',
            name='image',
            field=models.FileField(upload_to=b'images/%Y/%m/%d', blank=True),
        ),
    ]
