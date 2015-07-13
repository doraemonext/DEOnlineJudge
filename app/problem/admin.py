# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from app.problem.models import Problem, ProblemCategory, ProblemSample, Category


class ProblemCategoryInline(admin.StackedInline):
    model = ProblemCategory
    min_num = 1


class ProblemSampleInline(admin.TabularInline):
    model = ProblemSample
    min_num = 1


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    change_form_template = 'problem/admin/change_form.html'
    list_display = ('title', 'source', 'judge_type', 'time_limit', 'memory_limit', 'data_input_extension',
                    'data_output_extension', 'create_datetime')
    list_filter = ('title', 'source', 'judge_type', 'time_limit', 'memory_limit', 'data_input_extension',
                   'data_output_extension', 'create_datetime')
    search_fields = ['title', 'source']
    inlines = [ProblemCategoryInline, ProblemSampleInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', )
    list_filter = ('title', )
    search_fields = ['title']
