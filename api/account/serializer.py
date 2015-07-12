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


class RegistrationSerializer(serializers.Serializer):
    username = serializers.CharField(error_messages={'blank': '用户名不能为空'}, validators=[
        validator.MinValue('用户名', 2),
        validator.MaxValue('用户名', 30),
        validator.SafeValue('用户名'),
    ])
    email = serializers.CharField(error_messages={'blank': '邮箱不能为空'}, validators=[
        validator.EmailValue('邮箱'),
    ])
    password = serializers.CharField(max_length=128, error_messages={'blank': '密码不能为空'}, validators=[
        validator.MinValue('密码', 4),
        validator.MaxValue('密码', 64),
    ])
    confirm_password = serializers.CharField(max_length=128, error_messages={'blank': '确认密码不能为空'}, validators=[
        validator.MinValue('确认密码', 4),
        validator.MaxValue('确认密码', 64),
    ])
    nickname = serializers.CharField(error_messages={'blank': '昵称不能为空'}, validators=[
        validator.MinValue('昵称', 2),
        validator.MaxValue('昵称', 30),
        validator.SafeValue('昵称'),
    ])
    next = serializers.CharField(max_length=255, required=False, allow_blank=True)

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError('两次密码输入不一致')
        return attrs
