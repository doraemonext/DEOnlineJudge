# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0002_auto_20150712_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='data_input_extension',
            field=models.CharField(default='', max_length=32, verbose_name='\u6570\u636e\u8f93\u5165\u6587\u4ef6\u6269\u5c55\u540d'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='problem',
            name='data_output_extension',
            field=models.CharField(default='', max_length=32, verbose_name='\u6570\u636e\u8f93\u51fa\u6587\u4ef6\u6269\u5c55\u540d'),
            preserve_default=False,
        ),
    ]
