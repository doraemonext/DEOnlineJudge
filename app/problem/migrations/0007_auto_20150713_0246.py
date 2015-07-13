# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0006_auto_20150713_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='tips',
            field=models.TextField(verbose_name='\u63d0\u793a'),
        ),
    ]
