# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.db import models


class Node(models.Model):
    name = models.CharField('节点名称', max_length=64)
    host = models.CharField('节点地址', max_length=64)
    port = models.IntegerField('节点端口')

    class Meta:
        verbose_name = '评测节点表'
        verbose_name_plural = '评测节点表'
        db_table = 'node'
