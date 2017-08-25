# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=100, default=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.CharField(max_length=11, default=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='postcodes',
            field=models.CharField(max_length=6, default=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='receiver',
            field=models.CharField(max_length=20, default=''),
        ),
    ]
