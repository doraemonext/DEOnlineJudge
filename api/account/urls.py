# -*- coding: utf-8 -*-

from django.conf.urls import url

from api.account.views import RegistrationAPI, LoginAPI, LogoutAPI

urlpatterns = [
    url(r'^login/$', RegistrationAPI.as_view(), name='registration'),
    url(r'^login/$', LoginAPI.as_view(), name='login'),
    url(r'^logout/$', LogoutAPI.as_view(), name='logout'),
]
