from django.db import models


class SysSendEmail(models.Model):
    ops_type = ((0, u'默认发送'), (1, u'订阅行业推荐'), (2, u'主办方审核'), (3, u'下单成功'), (4, u'编辑通过会议审核'), (5, u'邀请函'))
    send_status = ((0, u'待发送'), (1, u'发送成功'), (2, u'发送失败'))

    event_id = models.IntegerField(u'活动ID', blank=True, null=True)
    create_time = models.DateTimeField(blank=True, auto_now_add=True, verbose_name='创建时间', help_text='创建时间')
    update_time = models.DateTimeField(blank=True, auto_now=True, verbose_name='更新时间', help_text='更新时间')
    is_delete = models.BooleanField(default=0, verbose_name='是否逻辑删除', help_text='是否逻辑删除')
    operation_type = models.PositiveSmallIntegerField(verbose_name=u'发送操作类型', default=0, choices=ops_type)
    msg_data = models.TextField(verbose_name='发送信息内容', help_text="JSON格式存储发送信息内容", null=True, blank=True)
    template_id = models.IntegerField(u'模版ID', blank=True, null=True)
    send_flag = models.BooleanField(default=0, verbose_name='是否发送', help_text='是否发送')  # 针对非即时发送，判断是否需要发送消息
    status = models.PositiveSmallIntegerField(verbose_name=u'投递状态', default=0, choices=send_status)
    email = email = models.EmailField(max_length=50, verbose_name=u'邮箱', blank=True, null=True)
    tag_id = models.IntegerField(u'邮件服务标记', blank=True, null=True)

    class Meta:
        db_table = 'sys__common_send_email'
        verbose_name = u'活动管理'
        verbose_name_plural = verbose_name


class SysSendSms(models.Model):
    class Meta:
        db_table = 'sys__common_send_sms'
        verbose_name = u'活动管理'
        verbose_name_plural = verbose_name
