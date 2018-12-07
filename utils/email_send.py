#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2018-12-07 09:37'

import os
import django

# 单个脚本调用django需要这样设置
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from random import Random

from django.core.mail import send_mail

from mysite.settings import WEB_DOMAIN, EMAIL_FROM


def random_str(randomLength=8):
    str = ""
    chars = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"   # 62
    length = len(chars) - 1    # 61, 从0开始计数
    random = Random()
    for i in range(randomLength):
        str += chars[random.randint(0, length)]
    return str


def send_register_email(email, send_type="register"):
    # setting email content

    code = random_str()
    email_title = ""
    email_body = ""

    if send_type == "register":
        email_title = "测试--在线注册激活链接"
        # email_body = "请点击下面的链接激活你的账号: http://127.0.0.1:8000/active/{0}".format(code)
        email_body = "请点击下面的链接激活你的账号: http://{0}/active/{1}".format(WEB_DOMAIN, code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])      # settings中配置邮件发送参数, recipent must be list type
        if send_status:
            pass

    elif send_type == "forget":
        email_title = "测试--密码重置链接"
        email_body = "请点击下面的链接重置您的账号密码: http://{0}/reset/{1}".format(WEB_DOMAIN, code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])   # settings中配置邮件发送参数, recipent must be list type
        if send_status:
            pass

    elif send_type == "update_email":
        email_title = "测试--邮箱修改验证码"
        email_body = "您的修改邮箱验证码为{0}".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM,
                                [email])  # settings中配置邮件发送参数, recipent must be list type
        if send_status:
            pass


if __name__ == '__main__':

    ret = send_register_email("xxxxxx@xxxx.com", send_type="register")
    print(ret)







