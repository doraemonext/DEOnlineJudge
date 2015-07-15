# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from app.node.models import Node


@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'host', 'port')
    list_filter = ('name', 'host', 'port')
    search_fields = ['name']
