# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.http import Http404
from django.views.generic import TemplateView

from system.users.models import User
from app.record.models import Record
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


class UsersView(TemplateView):
    template_name = 'account/users.html'

    def get_context_data(self, **kwargs):
        users = User.objects.all().order_by('-id')
        for user in users:
            record = Record.objects.filter(user=user)
            user.total_sum = record.count()
            record = record.filter(status='AC').values_list('problem', flat=True).distinct()
            user.ac_sum = record.count()
            if user.total_sum > 0:
                user.percent = int(float(user.ac_sum) / user.total_sum * 100)
            else:
                user.percent = 0

        context = super(UsersView, self).get_context_data(**kwargs)
        context['users'] = users
        return context


class UserDetailView(TemplateView):
    template_name = 'account/user_detail.html'

    def get_context_data(self, **kwargs):
        try:
            user = User.objects.get(pk=self.kwargs.get('id'))
        except User.DoesNotExist:
            raise Http404()
        record = Record.objects.filter(user=user)
        user.total_sum = record.count()
        record = record.filter(status='AC').values_list('problem', flat=True).distinct()
        user.ac_sum = record.count()
        if user.total_sum > 0:
            user.percent = int(float(user.ac_sum) / user.total_sum * 100)
        else:
            user.percent = 0

        records = Record.objects.filter(user=user).order_by('-create_datetime')
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context['current_user'] = user
        context['records'] = records
        return context
