# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.db import models

from system.users.models import User


class Problem(models.Model):
    title = models.CharField('标题', max_length=50)
    description = models.TextField('题目描述')
    input_format = models.TextField('输入格式')
    output_format = models.TextField('输出格式')
    limit = models.TextField('限制条件', max_length=256)
    source = models.CharField('题目来源', max_length=256)
    judge_type = models.CharField('判题类型', max_length=6)
    time_limit = models.IntegerField('时间限制(ms)')
    memory_limit = models.IntegerField('内存限制(MB)')
    tips = models.CharField('提示', max_length=256)
    data_input_extension = models.CharField('数据输入文件扩展名', max_length=32)
    data_output_extension = models.CharField('数据输出文件扩展名', max_length=32)
    create_datetime = models.DateTimeField('创建时间', auto_now_add=True)
    update_datetime = models.DateTimeField('更新时间', auto_now=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = '题目表'
        verbose_name_plural = '题目表'
        db_table = 'problem'


class Category(models.Model):
    title = models.CharField('分类名', max_length=128)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = '分类表'
        verbose_name_plural = '分类表'
        db_table = 'category'


class ProblemSample(models.Model):
    problem = models.ForeignKey(Problem, verbose_name='所属题目')
    sample_input = models.TextField('样例输入')
    sample_output = models.TextField('样例输出')

    class Meta:
        verbose_name = '题目样例表'
        verbose_name_plural = '题目样例表'
        db_table = 'sample'


class ProblemCategory(models.Model):
    problem = models.ForeignKey(Problem, verbose_name='所属题目')
    category = models.ForeignKey(Category, verbose_name='所属分类')

    class Meta:
        verbose_name = '题目分类表'
        verbose_name_plural = '题目分类表'
        db_table = 'problem_category'


class ProblemDiscussion(models.Model):
    problem = models.ForeignKey(Problem, verbose_name='所属题目')
    user = models.ForeignKey(User, verbose_name='所属用户')
    parent = models.ForeignKey('self', verbose_name='父亲评论')
    content = models.TextField('讨论内容')
    create_datetime = models.DateTimeField('创建时间', auto_now_add=True)
    update_datetime = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        verbose_name = '题目讨论表'
        verbose_name_plural = '题目讨论表'
        db_table = 'problem_discussion'
