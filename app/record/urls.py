# -*- coding: utf-8 -*-

from django.conf.urls import include, url

from app.record.views import RecordListView, RecordDetailView

urlpatterns = [
    url(r'^$', RecordListView.as_view(), name='list'),
    url(r'^(?P<id>[0-9]+)/$', RecordDetailView.as_view(), name='detail'),
]
