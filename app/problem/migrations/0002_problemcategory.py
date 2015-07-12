# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProblemCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128, verbose_name='\u5206\u7c7b\u540d')),
                ('problem', models.ForeignKey(verbose_name='\u6240\u5c5e\u9898\u76ee', to='problem.Problem')),
            ],
            options={
                'db_table': 'category',
                'verbose_name': '\u9898\u76ee\u5206\u7c7b\u8868',
                'verbose_name_plural': '\u9898\u76ee\u5206\u7c7b\u8868',
            },
        ),
    ]
