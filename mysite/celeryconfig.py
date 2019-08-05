#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2018-12-18 11:09'

from datetime import timedelta

import djcelery

djcelery.setup_loader()

# 设置队列，不然会用默认的
CELERY_QUEUES = {
    # 定时任务
    'beat_tasks': {
        'exchange': 'beat_tasks',
        'exchange_type': 'direct',
        'binding_key': 'beat_tasks'
    },
    # 普通任务
    'work_queue': {
        'exchange': 'work_queue',
        'exchange_type': 'direct',
        'binding_key': 'work_queue'
    }

}

# 设置默认队列
CELERY_DEFAULT_QUEUE = 'work_queue'

CELERY_IMPORTS = (
    'course.tasks',
)

# 非常重要,有些情况下可以防止死锁
CELERYD_FORCE_EXECV = True

# 设置并发worker数数量
CELERYD_CONCURRENCY = 4

# 允许重试
CELERY_ACKS_LATE = True

# 每个worker最多执行完100个任务就会被销毁，可防止内存泄露
CELERYD_MAX_TASKS_PER_CHILD = 50

# 单个任务的最大运行时间， 超过此值则会被SIGKILL信号杀死
CELERYD_TASK_TIME_LIMIT = 12 * 30  # 单位秒


CELERYBEAT_SCHEDULE = {
    'task1': {
        'task': 'course-task',
        'schedule': timedelta(seconds=5),
        # 使用指定队列
        'options': {
            'queue': 'beat_tasks'
        }
    }
}

