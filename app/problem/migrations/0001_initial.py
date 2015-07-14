# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128, verbose_name='\u5206\u7c7b\u540d')),
            ],
            options={
                'db_table': 'category',
                'verbose_name': '\u5206\u7c7b\u8868',
                'verbose_name_plural': '\u5206\u7c7b\u8868',
            },
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='\u6807\u9898')),
                ('description', models.TextField(verbose_name='\u9898\u76ee\u63cf\u8ff0', blank=True)),
                ('input_format', models.TextField(verbose_name='\u8f93\u5165\u683c\u5f0f', blank=True)),
                ('output_format', models.TextField(verbose_name='\u8f93\u51fa\u683c\u5f0f', blank=True)),
                ('limit', models.TextField(max_length=256, verbose_name='\u9650\u5236\u6761\u4ef6', blank=True)),
                ('tips', models.TextField(verbose_name='\u63d0\u793a', blank=True)),
                ('source', models.CharField(max_length=256, verbose_name='\u9898\u76ee\u6765\u6e90')),
                ('judge_type', models.CharField(max_length=6, verbose_name='\u5224\u9898\u7c7b\u578b')),
                ('time_limit', models.IntegerField(verbose_name='\u65f6\u95f4\u9650\u5236(ms)')),
                ('memory_limit', models.IntegerField(verbose_name='\u5185\u5b58\u9650\u5236(MB)')),
                ('data_input_extension', models.CharField(max_length=32, verbose_name='\u6570\u636e\u8f93\u5165\u6587\u4ef6\u6269\u5c55\u540d')),
                ('data_output_extension', models.CharField(max_length=32, verbose_name='\u6570\u636e\u8f93\u51fa\u6587\u4ef6\u6269\u5c55\u540d')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_datetime', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('category', models.ForeignKey(verbose_name='\u5206\u7c7b', blank=True, to='problem.Category', null=True)),
            ],
            options={
                'db_table': 'problem',
                'verbose_name': '\u9898\u76ee\u8868',
                'verbose_name_plural': '\u9898\u76ee\u8868',
            },
        ),
        migrations.CreateModel(
            name='ProblemDiscussion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(verbose_name='\u8ba8\u8bba\u5185\u5bb9')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_datetime', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('parent', models.ForeignKey(verbose_name='\u7236\u4eb2\u8bc4\u8bba', to='problem.ProblemDiscussion')),
                ('problem', models.ForeignKey(verbose_name='\u6240\u5c5e\u9898\u76ee', to='problem.Problem')),
                ('user', models.ForeignKey(verbose_name='\u6240\u5c5e\u7528\u6237', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'problem_discussion',
                'verbose_name': '\u9898\u76ee\u8ba8\u8bba\u8868',
                'verbose_name_plural': '\u9898\u76ee\u8ba8\u8bba\u8868',
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
    ]
