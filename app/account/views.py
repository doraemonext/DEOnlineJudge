# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.views.generic import TemplateView

from lib.tools.mixin import AnonymousRequiredMixin


class LoginView(AnonymousRequiredMixin, TemplateView):
    template_name = 'account/login.html'

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', '')
        return context

    def get_redirect_url(self, next):
        if next:
            return next
        else:
            return reverse('index:index')

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if request.user.is_authenticated():
            return HttpResponseRedirect(self.get_redirect_url(context['next']))
        return self.render_to_response(context)


class RegistrationView(AnonymousRequiredMixin, TemplateView):
    template_name = 'account/registration.html'

    def get_context_data(self, **kwargs):
        context = super(RegistrationView, self).get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', '')
        return context

    def get_redirect_url(self, next):
        if next:
            return next
        else:
            return reverse('index:index')

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if request.user.is_authenticated():
            return HttpResponseRedirect(self.get_redirect_url(context['next']))
        return self.render_to_response(context)
