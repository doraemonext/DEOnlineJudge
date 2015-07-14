"""DEOnlineJudge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
"""
from __future__ import absolute_import, unicode_literals

from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()
admin.site.site_header = 'DE Online Judge'

urlpatterns = [
    url(r'^$', include('app.index.urls', namespace='index')),
    url(r'^api/', include('api.urls', namespace='api')),
    url(r'^account/', include('app.account.urls', namespace='account')),
    url(r'^problem/', include('app.problem.urls', namespace='problem')),
    url(r'^record/', include('app.record.urls', namespace='record')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
]
