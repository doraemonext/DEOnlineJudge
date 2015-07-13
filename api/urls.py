# -*- coding: utf-8 -*-

from django.conf.urls import url, include

urlpatterns = [
    url(r'^account/', include('api.account.urls', namespace='account')),
    url(r'^problem/', include('api.problem.urls', namespace='problem')),
]
