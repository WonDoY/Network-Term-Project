# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('omok', '0003_omokboard'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='roominfo',
            name='full',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='roominfo',
            name='user1',
            field=models.CharField(default='none', max_length=15),
        ),
        migrations.AddField(
            model_name='roominfo',
            name='user2',
            field=models.CharField(default='none', max_length=15),
        ),
    ]
