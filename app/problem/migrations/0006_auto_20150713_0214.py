# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0005_auto_20150713_0204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='judge_type',
            field=models.CharField(max_length=6, verbose_name='\u5224\u9898\u7c7b\u578b'),
        ),
    ]
