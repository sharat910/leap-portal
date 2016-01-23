# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0008_puser_alumni'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumni',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('about', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('link', models.TextField(blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='puser',
            name='alumni',
        ),
        migrations.AddField(
            model_name='puser',
            name='contact',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='puser',
            name='fbprofile',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='puser',
            name='weblink',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
