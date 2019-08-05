#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2018-12-18 11:12'

import time
from celery.task import Task

class CourseTask(Task):

    name = 'course-task'

    def run(self, *args, **kwargs):
        print('start course task')
        time.sleep(4)
        print("args={}, kwargs={}".format(args, kwargs))
        print('end course task')
