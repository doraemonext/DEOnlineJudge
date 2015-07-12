# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index/index.html'
