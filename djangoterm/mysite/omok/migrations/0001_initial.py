# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='omokBoard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('board', models.TextField()),
                ('room_num', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='RoomInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=15)),
                ('pull', models.IntegerField(default=0)),
                ('user1', models.CharField(default='none', max_length=15)),
                ('user2', models.CharField(default='none', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=15)),
            ],
        ),
    ]
