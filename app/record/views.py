# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView
from django.http import Http404

from app.record.models import Record, RecordDetail


class RecordListView(TemplateView):
    template_name = 'record/list.html'

    def get_context_data(self, **kwargs):
        record_list = Record.objects.order_by('-create_datetime')
        paginator = Paginator(record_list, 20)
        page = self.request.GET.get('page')
        try:
            records = paginator.page(page)
        except PageNotAnInteger:
            records = paginator.page(1)
        except EmptyPage:
            records = paginator.page(paginator.num_pages)

        context = super(RecordListView, self).get_context_data(**kwargs)
        context['records'] = records
        return context


class RecordDetailView(TemplateView):
    template_name = 'record/detail.html'

    def get_context_data(self, **kwargs):
        record_id = self.kwargs.get('id')
        queryset = Record.objects.filter(pk=record_id)
        if not queryset.exists():
            raise Http404()
        problem = queryset[0]

        context = super(RecordDetailView, self).get_context_data(**kwargs)
        return context
