# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from django.db.models import Count

from app.record.models import Record
from app.problem.models import Problem
from system.users.models import User


class IndexView(TemplateView):
    template_name = 'index/index.html'

    def get_context_data(self, **kwargs):
        ac_rank = Record.objects.filter(status='AC').values('user').annotate(total=Count('user')).order_by('-total')
        total_rank = Record.objects.all().values('user').annotate(total=Count('user')).order_by('-total')
        for rank in ac_rank:
            user = User.objects.filter(pk=rank['user'])
            rank['user'] = user
        for rank in total_rank:
            user = User.objects.filter(pk=rank['user'])
            rank['user'] = user
        problems = Problem.objects.all().order_by('-create_datetime')[:15]
        for problem in problems:
            record = Record.objects.filter(problem=problem)
            problem.total_sum = record.count()
            record = record.filter(status='AC')
            problem.ac_sum = record.count()

        context = super(IndexView, self).get_context_data()
        context['ac_rank'] = ac_rank
        context['total_rank'] = total_rank
        context['problems'] = problems
        return context
