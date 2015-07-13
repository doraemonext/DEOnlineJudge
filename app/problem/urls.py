# -*- coding: utf-8 -*-

from django.conf.urls import include, url

from app.problem.views import ProblemListView, ProblemDetailView, ProblemSubmitView

urlpatterns = [
    url(r'^$', ProblemListView.as_view(), name='list'),
    url(r'^(?P<id>[0-9]+)/$', ProblemDetailView.as_view(), name='detail'),
    url(r'^(?P<id>[0-9]+)/submit/$', ProblemSubmitView.as_view(), name='submit'),
]
