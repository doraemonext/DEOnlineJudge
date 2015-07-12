# -*- coding: utf-8 -*-

from django.conf.urls import include, url

from app.problem.views import ProblemListView, ProblemDetailView

urlpatterns = [
    url(r'^list/$', ProblemListView.as_view(), name='list'),
    url(r'^detail/(?P<id>[0-9]+)/$', ProblemDetailView.as_view(), name='detail'),
]