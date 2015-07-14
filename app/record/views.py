# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView
from django.http import Http404
from django.db.models import Q

from app.record.models import Record, RecordDetail


class RecordListView(TemplateView):
    template_name = 'record/list.html'

    def get_context_data(self, **kwargs):
        record_list = Record.objects.all().order_by('-create_datetime')

        search_record = self.request.GET.get('record', '')
        search_problem = self.request.GET.get('problem', '')
        search_user = self.request.GET.get('user', '')
        search_language = self.request.GET.get('language', '')
        if search_record:
            if search_record.isdigit():
                record_list = record_list.filter(pk=search_record)
            else:
                record_list = record_list.filter(pk=0)  # 清空记录
        if search_problem:
            if search_problem.isdigit():
                record_list = record_list.filter(Q(problem__title=search_problem) | Q(problem__pk=search_problem))
            else:
                record_list = record_list.filter(problem__title=search_problem)
        if search_user:
            record_list = record_list.filter(Q(user__nickname=search_user) | Q(user__username=search_user))
        if search_language:
            record_list = record_list.filter(language=search_language)

        paginator = Paginator(record_list, 20)
        page = self.request.GET.get('page')
        try:
            records = paginator.page(page)
        except PageNotAnInteger:
            records = paginator.page(1)
        except EmptyPage:
            records = paginator.page(paginator.num_pages)

        context = super(RecordListView, self).get_context_data(**kwargs)
        context['search_record'] = search_record
        context['search_problem'] = search_problem
        context['search_user'] = search_user
        context['search_language'] = search_language

        context['records'] = records
        return context


class RecordDetailView(TemplateView):
    template_name = 'record/detail.html'

    def get_context_data(self, **kwargs):
        record_id = self.kwargs.get('id')
        queryset = Record.objects.filter(pk=record_id)
        if not queryset.exists():
            raise Http404()
        record = queryset[0]

        context = super(RecordDetailView, self).get_context_data(**kwargs)
        return context
