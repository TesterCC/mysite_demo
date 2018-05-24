#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/24 14:40'

import logging

from django.contrib.auth.models import User, Group
from rest_framework import serializers

log = logging.getLogger('testdemo')


# http://www.django-rest-framework.org/tutorial/quickstart/
# hyperlinking is good RESTful design

log.debug("test <testdemo> log record1")
log.info("test <testdemo> log record2")


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
