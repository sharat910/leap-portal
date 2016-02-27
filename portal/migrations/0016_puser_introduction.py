# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import portal.validators


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0015_auto_20160226_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='puser',
            name='introduction',
            field=models.FileField(blank=True, null=True, upload_to=b'intros/', validators=[portal.validators.validate_file_extension_intro]),
        ),
    ]
