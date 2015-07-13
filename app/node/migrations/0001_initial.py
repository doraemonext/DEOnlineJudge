# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64, verbose_name='\u8282\u70b9\u540d\u79f0')),
                ('host', models.CharField(max_length=64, verbose_name='\u8282\u70b9\u5730\u5740')),
                ('port', models.IntegerField(verbose_name='\u8282\u70b9\u7aef\u53e3')),
            ],
            options={
                'db_table': 'node',
                'verbose_name': '\u8bc4\u6d4b\u8282\u70b9\u8868',
                'verbose_name_plural': '\u8bc4\u6d4b\u8282\u70b9\u8868',
            },
        ),
    ]
