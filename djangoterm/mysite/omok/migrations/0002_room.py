# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('omok', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Playername', models.CharField(max_length=15)),
                ('Room_full', models.IntegerField(default=0)),
                ('Player1', models.CharField(max_length=15, default='Unknown')),
                ('Player2', models.CharField(max_length=15, default='Unknown')),
            ],
        ),
    ]
