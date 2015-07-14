# -*- coding: utf-8 -*-

from django.conf.urls import url

from app.account.views import LoginView, RegistrationView, UsersView, UserDetailView

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^registration/$', RegistrationView.as_view(), name='registration'),
    url(r'^user/$', UsersView.as_view(), name='users'),
    url(r'^user/(?P<id>[0-9]+)/$', UserDetailView.as_view(), name='user_detail'),
]
