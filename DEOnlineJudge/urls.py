"""DEOnlineJudge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
"""
from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^api/', include('api.urls', namespace='api')),
    url(r'^index/', include('app.index.urls', namespace='index')),
    url(r'^account/', include('app.account.urls', namespace='account')),
    url(r'^problem/', include('app.problem.urls', namespace='problem')),

    url(r'^admin/', include(admin.site.urls)),
]
