from django.db import models
from django.contrib.auth.models import User
from devs.models import WorkRecordsModel
from spmanage.models import OutlabModel

# 结算单
class CheckoutModel(models.Model):
    # 检修单
    workrecordid = models.ForeignKey(WorkRecordsModel,on_delete=models.DO_NOTHING,verbose_name ='检修单')
    # 工作成员
    workers = models.ManyToManyField(User,verbose_name ='工作成员')
    # 材料消耗
    outlabid = models.ManyToManyField(OutlabModel,verbose_name ='出库材料')
    # 人工费用
    workerfee = models.IntegerField(verbose_name='人工费用')
    # 创建时间
    crtime = models.DateTimeField(auto_now_add=True,verbose_name ='创建时间')
    # 修改时间
    uptime = models.DateTimeField(auto_now=True,verbose_name ='修改时间')

    def __str__(self):
        return self.workrecordid
    class Meta:
        ordering = ['crtime']
        verbose_name = '结算单'
        verbose_name_plural = '结算单'