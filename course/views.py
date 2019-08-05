#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.http import JsonResponse

from course.tasks import CourseTask

def do(request):
    # 执行异步任务
    print('start do request')
    # CourseTask.delay()
    # 另一种调用方法
    CourseTask.apply_async(args=('hello',), queue='work_queue')
    print('end do request')
    return JsonResponse({"status_code": 200, "result": "success"})
