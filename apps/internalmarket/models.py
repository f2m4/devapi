from django.db import models
from django.contrib.auth.models import User
from devs.models import WorkRecordsModel
from spmanage.models import OutlabModel
from humanres.models import ClassModel,GroupModel

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

# 检修人工费
class WorkerfeeModel(models.Model):
    workdate=models.DateTimeField(auto_now_add=True,verbose_name ='检修日期')
    classid=models.ForeignKey(ClassModel,on_delete=models.DO_NOTHING,verbose_name ='班组')
    forgrougid=models.ForeignKey(GroupModel,on_delete=models.DO_NOTHING,verbose_name ='服务单位')
    description = models.TextField(blank=True,verbose_name ='检修内容')
    sumfee=models.IntegerField(blank=True,verbose_name ='人工费总额')
    workinghours=models.CharField(max_length=30,verbose_name ='工时')
    userid=models.ForeignKey(User,on_delete=models.DO_NOTHING,verbose_name='施工人员')
    fee=models.IntegerField(blank=True,verbose_name ='人工单价')
    remarks=models.TextField(blank=True,verbose_name ='备注')
    # 创建时间
    crtime = models.DateTimeField(auto_now_add=True,verbose_name ='创建时间')
    # 修改时间
    uptime = models.DateTimeField(auto_now=True,verbose_name ='修改时间')

# 定额标签
class TagModel(models.Model):
    # 名称
    name = models.CharField(max_length=100,verbose_name ='名称')
    # 说明
    descript = models.CharField(max_length=100,verbose_name ='说明',blank=True)
    # 创建时间
    crtime = models.DateTimeField(auto_now_add=True,verbose_name ='创建时间')
    # 修改时间
    uptime = models.DateTimeField(auto_now=True,verbose_name ='修改时间')

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['id']
        verbose_name = '定额标签'
        verbose_name_plural = '定额标签'

#工作定额
class QingGongModel(models.Model):
    # 名称
    name = models.CharField(max_length=100,verbose_name ='作业名称')
    # 工时
    workingHours = models.CharField(max_length=100,verbose_name ='工时',blank=True)
    # 人工费
    fee=models.IntegerField(blank=True,verbose_name ='人工费')
    # 备注
    remark = models.CharField(max_length=100,verbose_name ='备注',blank=True)
    # 标签
    tag = models.ManyToManyField(TagModel,blank=True,verbose_name='所属部分')
    # 创建时间
    crtime = models.DateTimeField(auto_now_add=True,verbose_name ='创建时间')
    # 修改时间
    uptime = models.DateTimeField(auto_now=True,verbose_name ='修改时间')

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['crtime']
        verbose_name = '工作定额'
        verbose_name_plural = '工作定额'