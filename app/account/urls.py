# -*- coding: utf-8 -*-

from django.conf.urls import url

from app.account.views import LoginView, RegistrationView

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^registration/$', RegistrationView.as_view(), name='registration'),
]
