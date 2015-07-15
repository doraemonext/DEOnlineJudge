# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.contrib.auth import authenticate, login, logout, get_user_model, get_user
from django.core.urlresolvers import reverse
from django.db import IntegrityError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status, parsers

from api.account.serializer import LoginSerializer, RegistrationSerializer, UpdatePasswordSerializer, UpdateProfileSerializer


class RegistrationAPI(APIView):
    permission_classes = (permissions.AllowAny, )
    parser_classes = (parsers.FormParser, )

    def get_redirect_url(self, next):
        if next:
            return next
        else:
            return reverse('index:index')

    def post(self, request, format=None):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.data.get('username')
            password = serializer.data.get('password')
            email = serializer.data.get('email')
            nickname = serializer.data.get('nickname')
            redirect_url = serializer.data.get('next')

            User = get_user_model()
            try:
                User.objects.create_user(username=username, email=email, nickname=nickname, password=password)
            except IntegrityError:
                response = {
                    'username': [u'重复的用户名'],
                }
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                response = {
                    'redirect_url': self.get_redirect_url(redirect_url),
                }
                return Response(response, status=status.HTTP_200_OK)
            else:
                response = {
                    'non_field_errors': [u'注册新用户时发生异常'],
                }
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPI(APIView):
    permission_classes = (permissions.AllowAny, )
    parser_classes = (parsers.FormParser, )

    def get_redirect_url(self, next):
        if next:
            return next
        else:
            return reverse('index:index')

    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.data.get('username')
            password = serializer.data.get('password')
            redirect_url = serializer.data.get('next')

            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                response = {
                    'redirect_url': self.get_redirect_url(redirect_url),
                }
                return Response(response, status=status.HTTP_200_OK)
            else:
                response = {
                    'non_field_errors': [u'用户名或密码不正确'],
                }
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPI(APIView):
    permission_classes = (permissions.IsAuthenticated, )
    parser_classes = (parsers.FormParser, )

    def post(self, request):
        logout(request)
        response = {
            'redirect_url': reverse('index:index'),
        }
        return Response(response, status=status.HTTP_200_OK)


class UpdatePasswordAPI(APIView):
    permission_classes = (permissions.IsAuthenticated, )
    parser_classes = (parsers.FormParser, )

    def post(self, request):
        request_user = get_user(request)
        serializer = UpdatePasswordSerializer(data=request.data)
        if serializer.is_valid():
            old_password = serializer.data.get('old_password')
            password = serializer.data.get('password')

            if not request_user.check_password(old_password):
                response = {'non_field_errors': '检查旧密码时发生错误，请仔细核对'}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            request_user.set_password(password)
            request_user.save()
            user = authenticate(username=request_user.username, password=password)
            login(request, user)
            return Response({})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateProfileAPI(APIView):
    permission_classes = (permissions.IsAuthenticated, )
    parser_classes = (parsers.FormParser, )

    def post(self, request):
        request_user = get_user(request)
        serializer = UpdateProfileSerializer(data=request.data)
        if serializer.is_valid():
            nickname = serializer.data.get('nickname')
            email = serializer.data.get('email')

            request_user.nickname = nickname
            request_user.email = email
            request_user.save()
            return Response({})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
