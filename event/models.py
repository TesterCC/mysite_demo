from django.db import models


# Create your models here.
# for test online project

class SysEvent(models.Model):
    name = models.CharField(u'标题', max_length=100)
    create_time = models.DateTimeField(blank=True, auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(blank=True, auto_now=True, verbose_name='更新时间')
    is_delete = models.BooleanField(default=0, verbose_name='是否逻辑删除')

    class Meta:
        db_table = 'sys_new_event_info'
        verbose_name = u'活动管理'
        verbose_name_plural = verbose_name
