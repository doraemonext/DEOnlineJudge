# -*- coding: utf-8 -*-

from django.conf.urls import include, url

from app.index.views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
]
