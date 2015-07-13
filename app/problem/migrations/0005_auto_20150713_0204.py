# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0004_problemdiscussion'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='memory_limit',
            field=models.IntegerField(default=0, verbose_name='\u5185\u5b58\u9650\u5236(MB)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='problem',
            name='time_limit',
            field=models.IntegerField(default=0, verbose_name='\u65f6\u95f4\u9650\u5236(ms)'),
            preserve_default=False,
        ),
    ]
