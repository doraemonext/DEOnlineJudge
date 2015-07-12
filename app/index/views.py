# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.views.generic import TemplateView

from lib.tools.mixin import LoginRequiredMixin, AnonymousRequiredMixin


class IndexView(AnonymousRequiredMixin, TemplateView):
    template_name = 'index/index.html'
