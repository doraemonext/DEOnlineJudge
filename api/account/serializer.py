# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from rest_framework import serializers

from lib.tools import validator


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(error_messages={'blank': '用户名不能为空'}, validators=[
        validator.MinValue('用户名', 2),
        validator.MaxValue('用户名', 30),
        validator.SafeValue('用户名'),
    ])
    password = serializers.CharField(max_length=128, error_messages={'blank': '密码不能为空'}, validators=[
        validator.MinValue('密码', 4),
        validator.MaxValue('密码', 64),
    ])
    next = serializers.CharField(max_length=255, required=False, allow_blank=True)
