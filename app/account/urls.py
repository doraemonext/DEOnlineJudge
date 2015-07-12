# -*- coding: utf-8 -*-

from django.conf.urls import include, url

from app.account.views import LoginView

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
]
