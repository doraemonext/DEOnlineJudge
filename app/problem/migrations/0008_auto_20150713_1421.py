# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0007_auto_20150713_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='description',
            field=models.TextField(verbose_name='\u9898\u76ee\u63cf\u8ff0', blank=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='input_format',
            field=models.TextField(verbose_name='\u8f93\u5165\u683c\u5f0f', blank=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='limit',
            field=models.TextField(max_length=256, verbose_name='\u9650\u5236\u6761\u4ef6', blank=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='output_format',
            field=models.TextField(verbose_name='\u8f93\u51fa\u683c\u5f0f', blank=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='tips',
            field=models.TextField(verbose_name='\u63d0\u793a', blank=True),
        ),
    ]
