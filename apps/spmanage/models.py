from django.db import models
from django.contrib.auth.models import User


#厂家信息
class FactoryModel(models.Model):
    # 名称
    name = models.CharField(max_length=20,verbose_name ='名称')
    # 描述
    description = models.TextField(blank=True,verbose_name ='描述')
    # 地址
    addr = models.CharField(max_length=50,blank=True,verbose_name ='地址')
    # 联系人
    contactname = models.CharField(max_length=20,blank=True,verbose_name='联系人')
    # 联系电话
    phone = models.CharField(max_length=20,blank=True,verbose_name='联系电话')
    # 创建时间
    crtime = models.DateTimeField(auto_now_add=True,verbose_name ='创建时间')
    # 修改时间
    uptime = models.DateTimeField(auto_now=True,verbose_name ='修改时间')
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['crtime']
        verbose_name = '厂家信息'
        verbose_name_plural = '厂家信息'


# 备件类型
class TypeModel(models.Model):
    # 名称
    name = models.CharField(max_length=20,verbose_name ='名称')
    # 描述
    description = models.TextField(blank=True,verbose_name ='描述')
    # 创建时间
    crtime = models.DateTimeField(auto_now_add=True,verbose_name ='创建时间')
    # 修改时间
    uptime = models.DateTimeField(auto_now=True,verbose_name ='修改时间')
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['crtime']
        verbose_name = '备件类型'
        verbose_name_plural = '备件类型'


# 备件信息
class InfoModel(models.Model):
    # 名称
    name = models.CharField(max_length=20,verbose_name ='名称')
    # 描述
    description = models.TextField(blank=True,verbose_name ='描述')
    # 型号
    typenum = models.CharField(max_length=50,blank=True,verbose_name ='型号')
    # 厂家
    factoryid = models.ForeignKey(FactoryModel,on_delete=models.DO_NOTHING,verbose_name ='厂家')
    # 备件类型
    typeid = models.ForeignKey(TypeModel,on_delete=models.DO_NOTHING,verbose_name ='所属类型')
    # 创建时间
    crtime = models.DateTimeField(auto_now_add=True,verbose_name ='创建时间')
    # 修改时间
    uptime = models.DateTimeField(auto_now=True,verbose_name ='修改时间')
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['crtime']
        verbose_name = '备件信息'
        verbose_name_plural = '备件信息'

# 入库表
class InlabModel(models.Model):
    # 备件信息
    infoid = models.ForeignKey(InfoModel,on_delete=models.DO_NOTHING,verbose_name ='备件信息')
    # 数量
    num = models.IntegerField(verbose_name ='数量')
    # 单价
    unitprice = models.FloatField(blank=True,verbose_name ='单价')
    # 入库人
    userid = models.ForeignKey(User,on_delete=models.DO_NOTHING,verbose_name ='入库人')
    # 存放位置
    addr = models.CharField(max_length=50,blank=True,verbose_name ='存放位置')
    # 备注
    remark = models.CharField(max_length=50,blank=True,verbose_name ='备注')
    # 创建时间
    crtime = models.DateTimeField(auto_now_add=True,verbose_name ='创建时间')
    # 修改时间
    uptime = models.DateTimeField(auto_now=True,verbose_name ='修改时间')
    def __str__(self):
        return '{}--{}:{}'.format(self.infoid.name,self.infoid.typenum,self.num)
    class Meta:
        ordering = ['crtime']
        verbose_name = '入库'
        verbose_name_plural = '入库'

# 出库表
class OutlabModel(models.Model):
    # 入库id
    inlabid = models.ForeignKey(InlabModel,on_delete=models.DO_NOTHING,verbose_name ='入库id')
    # 数量
    num = models.IntegerField(verbose_name ='数量')
    # 领取人
    userid = models.ForeignKey(User,on_delete=models.DO_NOTHING,verbose_name ='领取人')
    # 备注
    remark = models.CharField(max_length=50,blank=True,verbose_name ='备注')
    # 创建时间
    crtime = models.DateTimeField(auto_now_add=True,verbose_name ='创建时间')
    # 修改时间
    uptime = models.DateTimeField(auto_now=True,verbose_name ='修改时间')
    def __str__(self):
        return '{}--{}:{}'.format(self.inlabid.infoid.name,self.inlabid.infoid.typenum,self.num)
    class Meta:
        ordering = ['crtime']
        verbose_name = '出库'
        verbose_name_plural = '出库'