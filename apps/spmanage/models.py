from django.db import models
from django.contrib.auth.models import User
from humanres.models import GroupModel
from devs.models import WorklineModel

#厂家信息
class FactoryModel(models.Model):
    # 名称
    name = models.CharField(max_length=20,verbose_name ='名称')
    # 描述
    description = models.TextField(blank=True,verbose_name ='描述',default='')
    # 地址
    addr = models.CharField(max_length=50,blank=True,verbose_name ='地址',default='')
    # 联系人
    contactname = models.CharField(max_length=20,blank=True,verbose_name='联系人',default='')
    # 联系电话
    phone = models.CharField(max_length=20,blank=True,verbose_name='联系电话',default='')
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


# 备件所属分类
class TypeModel(models.Model):
    # 名称
    name = models.CharField(max_length=20,verbose_name ='名称')
    # 描述
    description = models.TextField(blank=True,verbose_name ='描述',default='')
    # 创建时间
    crtime = models.DateTimeField(auto_now_add=True,verbose_name ='创建时间')
    # 修改时间
    uptime = models.DateTimeField(auto_now=True,verbose_name ='修改时间')
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['crtime']
        verbose_name = '备件分类'
        verbose_name_plural = '备件分类'

# 备件标签
class TagModel(models.Model):
    # 名称
    name = models.CharField(max_length=20,verbose_name ='名称')
    # 描述
    description = models.TextField(blank=True,verbose_name ='描述',default='')
    # 创建时间
    crtime = models.DateTimeField(auto_now_add=True,verbose_name ='创建时间')
    # 修改时间
    uptime = models.DateTimeField(auto_now=True,verbose_name ='修改时间')
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['crtime']
        verbose_name = '备件标签'
        verbose_name_plural = '备件标签'

# 备件信息
class InfoModel(models.Model):
    #所属生产线
    worklineid=models.ForeignKey(WorklineModel,on_delete=models.DO_NOTHING,verbose_name='所属生产线',blank=True)
    # 名称
    name = models.CharField(max_length=20,verbose_name ='名称')
    # 描述
    description = models.TextField(blank=True,verbose_name ='描述',default='')
    # 型号
    typenum = models.CharField(max_length=100,blank=True,verbose_name ='型号',default='')
    # 厂家
    factoryid = models.ForeignKey(FactoryModel,on_delete=models.DO_NOTHING,blank=True,default='',verbose_name ='厂家')
    # 备件类型
    typeid = models.ForeignKey(TypeModel,on_delete=models.DO_NOTHING,blank=True,verbose_name ='所属类型')
    # 备件标签
    tagid = models.ManyToManyField(TagModel,blank=True,verbose_name='标签')
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