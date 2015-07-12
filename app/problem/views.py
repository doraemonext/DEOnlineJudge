# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView

from app.problem.models import Problem, Category


class ProblemListView(TemplateView):
    template_name = 'problem/list.html'

    def get_context_data(self, **kwargs):
        problem_list = Problem.objects.all()
        paginator = Paginator(problem_list, 20)
        page = self.request.GET.get('page')
        try:
            problems = paginator.page(page)
        except PageNotAnInteger:
            problems = paginator.page(1)
        except EmptyPage:
            problems = paginator.page(paginator.num_pages)

        categories = Category.objects.all()

        context = super(ProblemListView, self).get_context_data(**kwargs)
        context['problems'] = problems
        context['categories'] = categories
        return context


class ProblemDetailView(TemplateView):
    template_name = 'problem/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProblemDetailView, self).get_context_data(**kwargs)
        context['title'] = 'This is a Program'
        return context
