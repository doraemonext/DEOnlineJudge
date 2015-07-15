# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('problem', '0001_initial'),
        ('node', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('source_code', models.TextField(verbose_name='\u4ee3\u7801')),
                ('status', models.CharField(default='WAIT', max_length=10, verbose_name='\u5f53\u524d\u72b6\u6001')),
                ('total_point', models.IntegerField(default=0, verbose_name='\u6d4b\u8bd5\u70b9\u6570')),
                ('score', models.IntegerField(default=0, verbose_name='\u5206\u6570')),
                ('time_used', models.IntegerField(default=0, verbose_name='\u6240\u7528\u65f6\u95f4')),
                ('memory_used', models.IntegerField(default=0, verbose_name='\u6240\u7528\u5185\u5b58')),
                ('message', models.TextField(default='', verbose_name='\u8fd0\u884c\u4fe1\u606f')),
                ('language', models.CharField(max_length=20, verbose_name='\u6240\u7528\u8bed\u8a00')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('node', models.ForeignKey(verbose_name='\u6240\u5c5e\u8bc4\u6d4b\u8282\u70b9', to='node.Node')),
                ('problem', models.ForeignKey(verbose_name='\u6240\u5c5e\u9898\u76ee', to='problem.Problem')),
                ('user', models.ForeignKey(verbose_name='\u6240\u5c5e\u7528\u6237', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'record',
                'verbose_name': '\u8bc4\u6d4b\u8bb0\u5f55\u8868',
                'verbose_name_plural': '\u8bc4\u6d4b\u8bb0\u5f55\u8868',
            },
        ),
        migrations.CreateModel(
            name='RecordDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=10, verbose_name='\u5f53\u524d\u72b6\u6001')),
                ('score', models.IntegerField(verbose_name='\u5206\u6570')),
                ('time_used', models.IntegerField(verbose_name='\u6240\u7528\u65f6\u95f4')),
                ('memory_used', models.IntegerField(verbose_name='\u6240\u7528\u5185\u5b58')),
                ('message', models.TextField(default='', verbose_name='\u8fd0\u884c\u4fe1\u606f')),
                ('record', models.ForeignKey(verbose_name='\u6240\u5c5e\u8bb0\u5f55', to='record.Record')),
            ],
            options={
                'db_table': 'record_detail',
                'verbose_name': '\u8bc4\u6d4b\u8bb0\u5f55\u8be6\u7ec6\u8868',
                'verbose_name_plural': '\u8bc4\u6d4b\u8bb0\u5f55\u8be6\u7ec6\u8868',
            },
        ),
    ]
