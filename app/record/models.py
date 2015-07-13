# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import

from django.db import models

from app.problem.models import Problem
from app.node.models import Node
from system.users.models import User


class Record(models.Model):
    problem = models.ForeignKey(Problem, verbose_name='所属题目')
    user = models.ForeignKey(User, verbose_name='所属用户')
    node = models.ForeignKey(Node, verbose_name='所属评测节点')
    status = models.CharField('当前状态', max_length=6)
    score = models.IntegerField('分数')
    time_used = models.IntegerField('所用时间')
    memory_used = models.IntegerField('所用内存')
    language = models.CharField('所用语言', max_length=20)
    create_datetime = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '评测记录表'
        verbose_name_plural = '评测记录表'
        db_table = 'record'


class RecordDetail(models.Model):
    record = models.ForeignKey(Record, verbose_name='所属记录')
    status = models.CharField('当前状态', max_length=6)
    score = models.IntegerField('分数')
    time_used = models.IntegerField('所用时间')
    memory_used = models.IntegerField('所用内存')

    class Meta:
        verbose_name = '评测记录详细表'
        verbose_name_plural = '评测记录详细表'
        db_table = 'record_detail'
