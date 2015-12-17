# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post_id', models.IntegerField()),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post_id', models.IntegerField()),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body', models.CharField(max_length=5000)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='Puser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('orgname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('joineddate', models.DateField()),
                ('location', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=200)),
                ('institution', models.CharField(max_length=200)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body', models.CharField(max_length=5000)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(to='portal.Puser')),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': 'Query',
                'verbose_name_plural': 'Queries',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(to='portal.Puser'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to='portal.Puser'),
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(to='portal.Puser'),
        ),
    ]
