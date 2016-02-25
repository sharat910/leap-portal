# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import portal.validators


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('details', models.FileField(upload_to=b'documents/%Y/%m/%d', validators=[portal.validators.validate_file_extension])),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='post_id',
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=0, to='portal.Post'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='puser',
            name='joineddate',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.ForeignKey(to='portal.Puser'),
        ),
    ]
