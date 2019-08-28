# -*- coding:utf-8 -*-

import datetime
import random
import os

from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse

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


def pay_for_tiantai_v2(request):
    """
    http://127.0.0.1:8000/pay_for_tiantai_v2
    :param request:
    :return:
    """
    current_date = datetime.datetime.now()

    if current_date.second % 2 == 0:
        # 1/2 B link, even number
        return redirect("https://www.baidu.com")

    # A link
    return redirect("https://github.com")

def pay_for_tiantai_v3(request):
    """
    http://127.0.0.1:8000/pay_for_tiantai_v3
    :param request:
    :return:
    """

    cur_path = os.getcwd()+"/devtest/"     # need change dir
    # print(cur_path)
    with open(cur_path+"config_link.txt", "r") as f:
        op_code = f.read().strip()

    if op_code == "1":

        current_date = datetime.datetime.now()

        if current_date.second % 2 == 0:
            # 1/2 B link, even number
            return redirect("https://www.baidu.com")

        # A link
        return redirect("https://www.163.com/")

    if op_code == "0":
        return redirect("https://www.163.com/")

def pay_for_tiantai_v4(request):
    """
    http://127.0.0.1:8000/pay_for_tiantai_v4
    :param request:
    :return:
    """

    cur_path = os.getcwd()+"/devtest/"     # need change dir
    # print(cur_path)
    with open(cur_path+"config_link.txt", "r") as f:
        op_code = f.read().strip()

    if op_code == "1":

        random_flag = random.choice((range(3)))
        print(f'flag value --> {random_flag}')
        if random_flag in [1, 2]:
            # B link
            return redirect("https://www.baidu.com")

        # A link
        return redirect("https://www.163.com/")

    if op_code == "0":
        return redirect("https://www.163.com/")


def set_pay_test_link(request, op_code):
    """
    127.0.0.1:8000/set_pay_test_link/ablink/on
    127.0.0.1:8000/set_pay_test_link/ablink/off
    :param request:
    :param op_code:
    :return:
    """
    print(op_code,type(op_code))  # for debug

    control_info = {"off": "0", "on": "1"}
    if op_code and control_info[op_code]:
        cur_path = os.getcwd() + "/devtest/"  # need change dir
        with open(cur_path + "config_link.txt", "w+") as f:
            f.write(control_info[op_code])
        return HttpResponse("{} set success".format(op_code))
    else:
        return HttpResponse("invalid request")

def get_pay_test_link_status(request):
    """
    127.0.0.1:8000/get_pay_test_link_status/
    :param request:
    :return:
    """

    control_info = {"0": "A/B link rate is closed.",
                    "1": "A/B link rate is open."}

    cur_path = os.getcwd()+"/devtest/"     # need change dir
    # print(cur_path)
    with open(cur_path+"config_link.txt", "r") as f:
        status_code = f.read().strip()

    if status_code and status_code in ["0", "1"]:
        return HttpResponse(control_info[status_code])
    else:
        return HttpResponse("config file error.")




def list_filter(request, city_cat_month, page=""):
    # page = page or 1
    print(request.path)
    print(city_cat_month)
    return None

