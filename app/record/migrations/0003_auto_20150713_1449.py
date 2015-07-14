# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0002_record_source_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='memory_used',
            field=models.IntegerField(default=0, verbose_name='\u6240\u7528\u5185\u5b58'),
        ),
        migrations.AlterField(
            model_name='record',
            name='score',
            field=models.IntegerField(default=0, verbose_name='\u5206\u6570'),
        ),
        migrations.AlterField(
            model_name='record',
            name='status',
            field=models.CharField(default='WAIT', max_length=10, verbose_name='\u5f53\u524d\u72b6\u6001'),
        ),
        migrations.AlterField(
            model_name='record',
            name='time_used',
            field=models.IntegerField(default=0, verbose_name='\u6240\u7528\u65f6\u95f4'),
        ),
    ]
