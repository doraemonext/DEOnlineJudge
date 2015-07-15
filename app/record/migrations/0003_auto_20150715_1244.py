# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0002_auto_20150715_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='memory_used',
            field=models.FloatField(default=0, verbose_name='\u6240\u7528\u5185\u5b58'),
        ),
    ]
