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


def pay_for_tiantai(request):
    """
    /pay_for_tiantai
    """

    current_date = datetime.datetime.now()

    # fake random
    mins_list = list(range(0,60))
    random_list = random.sample(mins_list, 15)

    if current_date.minute in random_list:
        # 1/4 B link
        return redirect("https://spay3.swiftpass.cn/spay/merchant/scanQr?qrId=4711e1c7-abd6-4cb9-a4b0-25dcd86f8ff2")

    # A link
    return redirect("https://qrcode.meituan.com/pay/1HDEGCPhUfv")

