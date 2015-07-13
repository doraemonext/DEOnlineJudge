# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import

from django.contrib.auth import authenticate, login, logout, get_user_model
from django.core.urlresolvers import reverse
from django.db import IntegrityError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status, parsers

from api.problem.serializer import ProblemSubmitSerializer
from app.record.models import Record
from app.node.models import Node
from app.problem.models import Problem


class ProblemSubmitAPI(APIView):
    permission_classes = (permissions.AllowAny, )
    parser_classes = (parsers.FormParser, )

    def post(self, request, format=None):
        serializer = ProblemSubmitSerializer(data=request.data)
        if serializer.is_valid():
            program_id = serializer.data.get('program')
            language = serializer.data.get('language')
            source_code = serializer.data.get('source_code')
            try:
                problem = Problem.objects.get(pk=program_id)
            except Problem.DoesNotExist:
                response = {
                    'problem_id': '不存在的题目ID'
                }
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            node = Node.objects.all()[0]

            Record.objects.create(
                problem=problem,
                user=request.user,
                node=node,
                source_code=source_code,
                language=language,
            )

            return Response({
                'redirect_url': reverse('record:list'),
            })
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)