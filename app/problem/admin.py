# -*- coding: utf-8 -*-

from django.contrib import admin

from app.problem.models import Problem, ProblemCategory, ProblemSample, Category

admin.site.register(Problem)
admin.site.register(Category)
