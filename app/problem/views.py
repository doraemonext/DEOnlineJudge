# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.views.generic import TemplateView


class ProblemListView(TemplateView):
    template_name = 'problem/list.html'


class ProblemDetailView(TemplateView):
    template_name = 'problem/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProblemDetailView, self).get_context_data(**kwargs)
        context['title'] = 'This is a Program'
        return context
