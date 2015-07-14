# -*- coding: utf-8 -*-

from django.conf.urls import url

from api.account.views import RegistrationAPI, LoginAPI, LogoutAPI, UpdatePasswordAPI, UpdateProfileAPI

urlpatterns = [
    url(r'^registration/$', RegistrationAPI.as_view(), name='registration'),
    url(r'^login/$', LoginAPI.as_view(), name='login'),
    url(r'^logout/$', LogoutAPI.as_view(), name='logout'),
    url(r'^update_password/$', UpdatePasswordAPI.as_view(), name='update_password'),
    url(r'^update_profile/$', UpdateProfileAPI.as_view(), name='update_profile'),
]
