# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0007_puser_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='puser',
            name='alumni',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
