# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, View
from django.http.response import HttpResponseRedirect
from django.db.models import Count

from app.record.models import Record
from app.problem.models import Problem
from system.users.models import User


class IndexView(View):
    def get(self, request):
        return HttpResponseRedirect(reverse('problem:list'))
