# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recorddetail',
            name='memory_used',
            field=models.FloatField(verbose_name='\u6240\u7528\u5185\u5b58'),
        ),
    ]
