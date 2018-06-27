# -*- coding:utf-8 -*-

import datetime
from django.shortcuts import render_to_response

# locals()可以直接将函数中所有的变量全部传给模板。当然这可能会传递一些多余的参数，有点浪费内存的嫌疑。


def current_datetime(request):
    current_date = datetime.datetime.now()
    return render_to_response('current_date.html', locals())

