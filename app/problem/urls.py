# -*- coding: utf-8 -*-

from django.conf.urls import include, url

from app.problem.views import ProblemListView

urlpatterns = [
    url(r'^list/$', ProblemListView.as_view(), name='list'),
]
