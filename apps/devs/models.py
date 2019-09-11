from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from humanres.models import GroupModel,ClassModel
from spmanage.models import InfoModel
import django.utils.timezone as timezone
# Create your models here.
# 生产线
class WorklineModel(models.Model):
    # 名称
    name = models.CharField(max_length=30,verbose_name ='名称')
    # 描述
    description = models.TextField(blank=True,verbose_name ='描述')
    # 所属车间
    groupid = models.ForeignKey(GroupModel,on_delete=models.DO_NOTHING,verbose_name ='所属车间')
    # 创建时间
    crtime = models.DateTimeField(auto_now_add=True,verbose_name ='创建时间')
    # 修改时间
    uptime = models.DateTimeField(auto_now=True,verbose_name ='修改时间')

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['crtime']
        verbose_name = '生产线'
        verbose_name_plural = '生产线'

# 设备
class DevsModel(models.Model):
    # 名称
    name = models.CharField(max_length=20,verbose_name ='名称')
    # 描述
    description = models.TextField(blank=True,verbose_name ='描述')
    # 所属生产线
    worklineid = models.ForeignKey(WorklineModel, on_delete=models.DO_NOTHING,verbose_name ='所属生产线')
    # 创建时间
    crtime = models.DateTimeField(auto_now_add=True,verbose_name ='创建时间')
    # 修改时间
    uptime = models.DateTimeField(auto_now=True,verbose_name ='修改时间')
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['crtime']
        verbose_name = '设备表'
        verbose_name_plural = '设备表'
# 设备包机人
class MainmanModel(models.Model):
    # 用户id
    uid = models.ForeignKey(User, on_delete=models.DO_NOTHING,verbose_name ='用户id')
    # 描述
    description = models.TextField(blank=True,verbose_name ='描述')
    # 包机设备
    devsid = models.ManyToManyField(DevsModel,blank=True,verbose_name ='包机设备')
    # 创建时间
    crtime = models.DateTimeField(auto_now_add=True,verbose_name ='创建时间')
    # 修改时间
    uptime = models.DateTimeField(auto_now=True,verbose_name ='修改时间')
    def __str__(self):
        return self.uid.username
    class Meta:
        ordering = ['crtime']
        verbose_name = '包机表'
        verbose_name_plural = '包机表'

# 设备报修记录
class DevRecordsModel(models.Model):
    onestar = "1"
    twostar = "2"
    threestar = "3"
    fourstar = "4"
    fivestar = "5"
    LEVEL_CHOICES = [
        (onestar, '稍后'),
        (twostar, '不重要不紧急'),
        (threestar, '不重要紧急'),
        (fourstar, '重要不紧急'),
        (fivestar, '重要紧急'),
    ]
    # 报修人id
    uid = models.ForeignKey(User, on_delete=models.DO_NOTHING,verbose_name ='报修人id')
    # 故障设备id
    devsid = models.ForeignKey(DevsModel,on_delete=models.DO_NOTHING,blank=True,verbose_name ='故障设备id')
    # 故障描述
    # description = models.TextField(blank=True,verbose_name ='描述')
    description = RichTextUploadingField(blank=True,verbose_name ='描述')
    # 故障等级
    level = models.CharField(
        max_length=2,
        choices=LEVEL_CHOICES,
        default=onestar,
    )
    # 创建时间
    crtime = models.DateTimeField(auto_now_add=True,verbose_name ='创建时间')
    # 修改时间
    uptime = models.DateTimeField(auto_now=True,verbose_name ='修改时间')
    def __str__(self):
        return self.devsid.name
    class Meta:
        ordering = ['-crtime']
        verbose_name = '报修记录'
        verbose_name_plural = '报修记录'

# 设备维修记录
class WorkRecordsModel(models.Model):
    # 检修人id
    uid = models.ForeignKey(User, on_delete=models.DO_NOTHING,verbose_name ='检修人id')
    # 设备报修记录id
    devRecordid = models.ForeignKey(DevRecordsModel,on_delete=models.DO_NOTHING,verbose_name ='设备报修记录id')
    # 故障处理描述
    description = RichTextUploadingField(blank=True,verbose_name ='故障处理描述')
    # 故障状态 False,正在维修.True,维修完成
    isfininsh = models.BooleanField(default=False,verbose_name ='故障状态')
    # 创建时间
    crtime = models.DateTimeField(auto_now_add=True,verbose_name ='创建时间')
    # 修改时间
    uptime = models.DateTimeField(auto_now=True,verbose_name ='修改时间')

    def __str__(self):
        return '{}正在{}，进行检修'.format(self.uid.username,self.devRecordid.name)
    class Meta:
        ordering = ['-crtime']
        verbose_name = '检修记录'
        verbose_name_plural = '检修记录'


class WorkRecModel(models.Model):
    #工作班组
    classId=models.ForeignKey(ClassModel,on_delete=models.DO_NOTHING,verbose_name='班组')
    # 设备名称
    devName=models.ForeignKey(DevsModel,on_delete=models.DO_NOTHING,verbose_name='设备名称')
    # 设备部位
    devPart = models.CharField(max_length=50, verbose_name='设备部位',blank=True)
    # 故障描述 可做富文本
    faultDescription=models.TextField(verbose_name='故障描述',blank=True)
    # 检修内容
    repairContent = models.TextField(verbose_name='检修内容',blank=True)
    # 工作分类
    workType=models.CharField(max_length=50, verbose_name='工作分类',blank=True)
    # 故障分类
    faultType=models.CharField(max_length=50, verbose_name='故障分类',blank=True)
    # 备件名称
    spareName=models.CharField(max_length=50, verbose_name='备件名称',blank=True)
    # 备件类型
    spareType=models.CharField(max_length=50, verbose_name='备件型号',blank=True)
    # 备件类型id 外键
    spareTypeId=models.ForeignKey(InfoModel,on_delete=models.DO_NOTHING,blank=True,null=True,verbose_name='备件编号')
    # 备件单位
    spareUnit=models.CharField(max_length=50, verbose_name='备件单位',blank=True)
    # 备件数量
    spareQuantity=models.CharField(max_length=50, verbose_name='备件数量',blank=True)
    # 参与人员
    participants=models.ManyToManyField(User,blank=True,verbose_name ='参与人员')
    # 故障分析描述
    description = RichTextUploadingField(blank=True,verbose_name ='故障分析描述')
    # 故障状态 False,正在维修.True,维修完成
    isfininsh = models.BooleanField(default=False,verbose_name ='故障状态')
    # 录入员
    recorder = models.ForeignKey(User,on_delete=models.DO_NOTHING,blank=True,null=True,related_name='recorder',verbose_name='录入员')
    # 开始时间
    bgTime=models.DateTimeField(verbose_name='开始时间',default=timezone.datetime(2019,1,1,12))
    # 结束时间
    edTime=models.DateTimeField(verbose_name='结束时间',default=timezone.datetime(2019,1,1,12))
    # 创建时间
    crtime = models.DateTimeField(auto_now_add=True,verbose_name ='创建时间')
    # 修改时间
    uptime = models.DateTimeField(auto_now=True,verbose_name ='修改时间')

    def __str__(self):
        return '{}正在，进行检修'.format(self.devName.name)
    class Meta:
        ordering = ['-crtime']
        verbose_name = '检修台帐'
        verbose_name_plural = '检修台帐'

# 时间测试
class TTModel(models.Model):
    # 名称
    name = models.CharField(max_length=30,verbose_name ='名称')
    # 出生日期
    bir=models.DateTimeField(verbose_name='出生日期')
    # 创建时间
    crtime = models.DateTimeField(auto_now_add=True,verbose_name ='创建时间')
    # 修改时间
    uptime = models.DateTimeField(auto_now=True,verbose_name ='修改时间')

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']
        verbose_name = '生日'
        verbose_name_plural = '生日'
