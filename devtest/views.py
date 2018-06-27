# -*- coding:utf-8 -*-

import datetime
from django.shortcuts import render_to_response


def current_datetime(request):
    current_date = datetime.datetime.now()
    return render_to_response('current_date.html', locals())