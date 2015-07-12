# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.views.generic import TemplateView


class ProblemListView(TemplateView):
    template_name = 'problem/list.html'
