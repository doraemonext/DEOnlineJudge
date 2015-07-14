# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0005_record_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='message',
            field=models.TextField(default='', verbose_name='\u8fd0\u884c\u4fe1\u606f'),
        ),
    ]
