# -*- coding: utf-8 -*-

from django.conf.urls import url

from api.problem.views import ProblemSubmitAPI

urlpatterns = [
    url(r'^submit/$', ProblemSubmitAPI.as_view(), name='submit'),
]
