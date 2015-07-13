# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('problem', '0003_auto_20150713_0005'),
    ]

    operations = [
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
    ]
