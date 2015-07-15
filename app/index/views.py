# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import View
from django.http.response import HttpResponseRedirect


class IndexView(View):
    def get(self, request):
        return HttpResponseRedirect(reverse('problem:list'))
