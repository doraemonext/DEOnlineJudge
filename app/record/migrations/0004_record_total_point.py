# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0003_auto_20150713_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='total_point',
            field=models.IntegerField(default=0, verbose_name='\u6d4b\u8bd5\u70b9\u6570'),
        ),
    ]
