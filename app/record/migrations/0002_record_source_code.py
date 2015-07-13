# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='source_code',
            field=models.TextField(default='', verbose_name='\u4ee3\u7801'),
            preserve_default=False,
        ),
    ]
