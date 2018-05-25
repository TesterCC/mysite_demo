#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/25 11:01'

from django.conf.urls import url
from snippets.views import snippet_list, snippet_detail

urlpatterns = [
    url(r'^snippets/$', snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', snippet_detail),    # http://127.0.0.1:8000/snippets/2/
]