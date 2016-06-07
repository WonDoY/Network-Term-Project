# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('omok', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('full', models.IntegerField(default=0)),
                ('user1', models.CharField(default='none', max_length=15)),
                ('user2', models.CharField(default='none', max_length=15)),
            ],
        ),
    ]
