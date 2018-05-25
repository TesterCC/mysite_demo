#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/25 11:01'

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from snippets.views import SnippetList, SnippetDetail

urlpatterns = [
    url(r'^snippets/$', SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', SnippetDetail.as_view()),    # http://127.0.0.1:8000/snippets/2/
]

# display as  http://example.com/api/items/4.json
urlpatterns = format_suffix_patterns(urlpatterns)

