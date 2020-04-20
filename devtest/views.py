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


def shuffle_str(s):
    from random import shuffle
    # 将字符串转换成列表
    str_list = list(s)
    # 调用random模块的shuffle函数打乱列表
    shuffle(str_list)
    # 将列表转字符串
    return ''.join(str_list)

def pay_for_tiantai_v5(request):   ## TODO yanxi 20200420 update to xiaorizi server
    """
    http://127.0.0.1:8000/pay_for_tiantai_v5
    对方需求 a 天台码出现3 b示范田码 出现7 （每10次）

    每10次访问:
    3 A天台码
    7 B示范田
    """

    cur_path = os.getcwd()+"/devtest/"     # need change dir "/devtest" is local path
    # print(cur_path)
    with open(cur_path+"config_link.txt", "r") as f:
        op_code = f.read().strip()

    if op_code == "1":
        with open(cur_path + "select_container.txt", "r") as f:
            select_pool_str = f.read().strip()
            print("select pool-->", select_pool_str)
            if select_pool_str:
                select_pool = list(select_pool_str)
            else:
                # 10次订单内 固定 分配比 是 可以控制的
                # 固定好 01 字符的比例, 然后排列随机,  每次取一个, 取完了, 再随机一组
                # 容量大了, 分布更随机一些, 容量小了, 数据更准确一点
                # jump_flag=1 走B示范田， jump_flag=0 走天台
                origin_pool = '0001111111'  # online

                random_pool = shuffle_str(origin_pool)
                with open(cur_path + "select_container.txt", "w+") as f:
                    new_select_pool = f.write(random_pool)
                    print("new select pool>>>", new_select_pool)

                with open(cur_path + "select_container.txt", "r") as f:
                    select_pool_str = f.read().strip()
                    print("select pool 2-->", select_pool_str)

                select_pool = list(select_pool_str)

            jump_flag = list(select_pool)[0]
            print("jump flag : ", jump_flag)
            if jump_flag == '1':
                # B link
                select_pool.pop(0)
                with open(cur_path + "select_container.txt", "w") as f:
                    f.write("".join(select_pool))
                return redirect("https://www.baidu.com")
            else:
                # A link
                select_pool.pop(0)
                with open(cur_path + "select_container.txt", "w") as f:
                    f.write("".join(select_pool))
                return redirect("https://www.aliyun.com")

    if op_code == "0":
        # A link
        return redirect("https://www.aliyun.com")

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


def verify_code_demo(request):
    '''
    https://www.jb51.net/article/161804.htm
    :param request:
    :return:
    '''
    # 引入绘图模块
    from PIL import Image, ImageDraw, ImageFont
    # 引入随机函数模块
    import random
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), random.randrange(20, 100))
    width = 100
    height = 50
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str = '1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str[random.randrange(0, len(str))]
    # 构造字体对象
    # font = ImageFont.truetype('楷体', 40)
    # 构造字体颜色
    fontcolor1 = (255, random.randrange(0, 255), random.randrange(0, 255))
    fontcolor2 = (255, random.randrange(0, 255), random.randrange(0, 255))
    fontcolor3 = (255, random.randrange(0, 255), random.randrange(0, 255))
    fontcolor4 = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], fill=fontcolor1)
    draw.text((25, 2), rand_str[1], fill=fontcolor2)
    draw.text((50, 2), rand_str[2], fill=fontcolor3)
    draw.text((75, 2), rand_str[3], fill=fontcolor4)
    # 释放画笔
    del draw
    # 存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    # 内存文件操作
    import io
    buf = io.BytesIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')


def get_check_code_image(request):
    from PIL import Image, ImageDraw, ImageFont
    import io

    _letter_cases = "abcdefghjkmnpqrstuvwxy"  # 小写字母，去除可能干扰的i，l，o，z
    _upper_cases = _letter_cases.upper()  # 大写字母
    _numbers = ''.join(map(str, range(3, 10)))  # 数字
    init_chars = ''.join([_letter_cases, _upper_cases, _numbers])

    width = 200
    height = 70

    g1 = random.randint(240, 255)
    b1 = random.randint(240, 255)
    k1 = random.randint(240, 255)

    bgcolor = (g1, b1, k1)

    image = Image.new('RGB', (width, height), bgcolor)
    # font = ImageFont.truetype('/Library/Fonts/arial.ttf', 40)
    font = ImageFont.truetype('/Library/Fonts/iNked God.ttf', 40)
    g = random.randint(10, 200)
    b = random.randint(10, 200)
    k = random.randint(10, 200)
    fontcolor = (g, b, k)
    # fontcolor = (45,157,169)
    draw = ImageDraw.Draw(image)
    rand_chars = random.sample(init_chars, 4)
    rand_str = ' %s ' % ' '.join(rand_chars)
    captcha_pos = request.GET.get('position', '')
    request.session['captcha%s' % captcha_pos] = ''.join(rand_chars)
    font_width, font_height = font.getsize(rand_str)

    draw.text(
        ((width - font_width) / 3, (height - font_height) / 3),
        rand_str,
        font=font,
        fill=fontcolor)

    del draw

    buf = io.BytesIO()
    # 将图片保存在内存中，文件类型为gif
    image.save(buf, 'GIF')

    return HttpResponse(buf.getvalue(), 'image/gif')