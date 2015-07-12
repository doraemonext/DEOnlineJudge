# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='\u6807\u9898')),
                ('description', models.TextField(verbose_name='\u9898\u76ee\u63cf\u8ff0')),
                ('input_format', models.TextField(verbose_name='\u8f93\u5165\u683c\u5f0f')),
                ('output_format', models.TextField(verbose_name='\u8f93\u51fa\u683c\u5f0f')),
                ('limit', models.TextField(max_length=256, verbose_name='\u9650\u5236\u6761\u4ef6')),
                ('source', models.CharField(max_length=256, verbose_name='\u9898\u76ee\u6765\u6e90')),
                ('judge_type', models.SmallIntegerField(verbose_name='\u5224\u9898\u7c7b\u578b')),
                ('tips', models.CharField(max_length=256, verbose_name='\u63d0\u793a')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_datetime', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
            ],
            options={
                'db_table': 'problem',
                'verbose_name': '\u9898\u76ee\u8868',
                'verbose_name_plural': '\u9898\u76ee\u8868',
            },
        ),
        migrations.CreateModel(
            name='ProblemSample',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sample_input', models.TextField(verbose_name='\u6837\u4f8b\u8f93\u5165')),
                ('sample_output', models.TextField(verbose_name='\u6837\u4f8b\u8f93\u51fa')),
                ('problem', models.ForeignKey(verbose_name='\u6240\u5c5e\u9898\u76ee', to='problem.Problem')),
            ],
            options={
                'db_table': 'sample',
                'verbose_name': '\u9898\u76ee\u6837\u4f8b\u8868',
                'verbose_name_plural': '\u9898\u76ee\u6837\u4f8b\u8868',
            },
        ),
        migrations.CreateModel(
            name='ProblemTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128, verbose_name='\u6807\u7b7e\u540d')),
                ('problem', models.ManyToManyField(to='problem.Problem', verbose_name='\u6240\u5c5e\u9898\u76ee')),
            ],
            options={
                'db_table': 'tags',
                'verbose_name': '\u9898\u76ee\u6807\u7b7e\u8868',
                'verbose_name_plural': '\u9898\u76ee\u6807\u7b7e\u8868',
            },
        ),
    ]
