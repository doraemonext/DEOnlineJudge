# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone


class UserManager(BaseUserManager):
    def _create_user(self, username, email, nickname, password, is_superuser=False, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, nickname=nickname,
                          is_active=True, is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, nickname, password, **extra_fields):
        return self._create_user(username, email, nickname, password, **extra_fields)

    def create_superuser(self, username, email, nickname, password, **extra_fields):
        return self._create_user(username, email, nickname, password, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(u'用户名', max_length=30, unique=True)
    email = models.EmailField(u'电子邮件地址', max_length=255)
    nickname = models.CharField(u'昵称', max_length=30)
    is_active = models.BooleanField(u'是否激活', default=False)
    date_joined = models.DateTimeField(u'注册日期', default=timezone.now)

    objects = UserManager()

    class Meta:
        verbose_name = '用户表'
        verbose_name_plural = '用户表'
        db_table = 'user'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'nickname']

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def __unicode__(self):
        return self.username
