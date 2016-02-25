# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import portal.validators


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_auto_20151226_0621'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('details', models.FileField(blank=True, null=True, upload_to=b'documents/%Y/%m/%d', validators=[portal.validators.validate_file_extension])),
                ('user', models.ForeignKey(to='portal.Puser')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('teamstrength', models.IntegerField()),
                ('workingarea', models.CharField(max_length=200)),
                ('achievements', models.TextField()),
                ('details', models.FileField(blank=True, null=True, upload_to=b'documents/%Y/%m/%d', validators=[portal.validators.validate_file_extension])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(to='portal.Puser')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
