#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/23 12:05'

from django.urls import path

from polls import views

urlpatterns = [

    path('', views.index, name='index'),
]
