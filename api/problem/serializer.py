# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from rest_framework import serializers


class ProblemSubmitSerializer(serializers.Serializer):
    problem = serializers.CharField(error_messages={'blank': '必须提交题目ID', 'required': '必须提交题目ID'})
    language = serializers.CharField(error_messages={'blank': '必须选择语言', 'required': '必须选择语言'})
    source_code = serializers.CharField(error_messages={'blank': '程序代码不能为空', 'required': '程序代码不能为空'})

    def validate_language(self, value):
        if value not in ['C', 'C++', 'Pascal']:
            raise serializers.ValidationError('语言选择错误')
        return value

    def validate_source_code(self, value):
        keywords = ['system', 'socket', 'shutdown', 'reboot', 'init 0', 'init 6', 'signal']
        for keyword in keywords:
            if keyword in value:
                raise serializers.ValidationError('代码中包含高危关键字，请检查并修改')
        return value