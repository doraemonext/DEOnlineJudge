# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView
from django.http import Http404

from app.problem.models import Problem, Category
from lib.tools.mixin import LoginRequiredMixin


class ProblemListView(TemplateView):
    template_name = 'problem/list.html'

    def get_context_data(self, **kwargs):
        problem_list = Problem.objects.all()

        search_problem_id = self.request.GET.get('problem_id', '')
        search_problem_title = self.request.GET.get('problem_title', '')
        search_category = self.request.GET.get('category', '')
        search_source = self.request.GET.get('source', '')
        if search_problem_id:
            if search_problem_id.isdigit():
                problem_list = problem_list.filter(pk=search_problem_id)
            else:
                problem_list = problem_list.filter(pk=0)  # 清空记录
        if search_problem_title:
            problem_list = problem_list.filter(title=search_problem_title)
        if search_category:
            problem_list = problem_list.filter(category__title=search_category)
        if search_source:
            problem_list = problem_list.filter(source=search_source)

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
        context['search_problem_id'] = search_problem_id
        context['search_problem_title'] = search_problem_title
        context['search_category'] = search_category
        context['search_source'] = search_source
        return context


class ProblemDetailView(TemplateView):
    template_name = 'problem/detail.html'

    def get_context_data(self, **kwargs):
        problem_id = self.kwargs.get('id')
        queryset = Problem.objects.filter(pk=problem_id)
        if not queryset.exists():
            raise Http404()
        problem = queryset[0]

        context = super(ProblemDetailView, self).get_context_data(**kwargs)
        context['problem_id'] = problem.pk
        context['title'] = problem.title
        context['description'] = problem.description
        context['input_format'] = problem.input_format
        context['output_format'] = problem.output_format
        context['sample'] = problem.problemsample_set.all()
        context['limit'] = problem.limit
        context['tips'] = problem.tips
        context['source'] = problem.source
        context['judge_type'] = problem.judge_type
        context['time_limit'] = problem.time_limit
        context['memory_limit'] = problem.memory_limit
        return context


class ProblemSubmitView(LoginRequiredMixin, TemplateView):
    template_name = 'problem/submit.html'

    def get_context_data(self, **kwargs):
        problem_id = self.kwargs.get('id')
        queryset = Problem.objects.filter(pk=problem_id)
        if not queryset.exists():
            raise Http404()
        problem = queryset[0]

        context = super(ProblemSubmitView, self).get_context_data(**kwargs)
        context['problem_id'] = problem.pk
        context['title'] = problem.title
        context['description'] = problem.description
        context['input_format'] = problem.input_format
        context['output_format'] = problem.output_format
        context['limit'] = problem.limit
        context['tips'] = problem.tips
        context['source'] = problem.source
        context['judge_type'] = problem.judge_type
        context['time_limit'] = problem.time_limit
        context['memory_limit'] = problem.memory_limit
        return context
