# -*- coding:utf-8 -*-

import datetime
import random

from django.shortcuts import render_to_response, redirect

# locals()可以直接将函数中所有的变量全部传给模板。当然这可能会传递一些多余的参数，有点浪费内存的嫌疑。


def current_datetime(request):
    current_date = datetime.datetime.now()
    current_date = current_date.strftime('%Y-%m-%d %H:%M:%S')
    return render_to_response('current_date.html', locals())


def pay_test(request):
    """
    http://127.0.0.1:8000/pay_test
    :param request:
    :return:
    """

    current_date = datetime.datetime.now()

    # fake random
    mins_list = list(range(0,60))
    random_list = random.sample(mins_list, 15)

    if current_date.minute in random_list:
        # print(random_list)
        # print(current_date.minute)
        # 1/4 B link
        return redirect("https://www.baidu.com")

    # print(random_list)
    # print(current_date.minute)
    # A link
    return redirect("https://github.com")


def list_filter(request, city_cat_month, page=""):
    # page = page or 1
    print(request.path)
    print(city_cat_month)
    return None

