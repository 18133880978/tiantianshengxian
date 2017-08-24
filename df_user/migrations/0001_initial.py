# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Areas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=20)),
                ('parea', models.ForeignKey(blank=True, null=True, to='df_user.Areas')),
            ],
            options={
                'db_table': 'areas',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('username', models.CharField(max_length=20)),
                ('passwd', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=30)),
                ('receiver', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('postcodes', models.CharField(max_length=6)),
                ('mobile', models.CharField(max_length=11)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
