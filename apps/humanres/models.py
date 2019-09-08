from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# 部门
class GroupModel(models.Model):
    # 名称
    name = models.CharField(max_length=30,verbose_name ='名称')
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
        verbose_name = '部门表'
        verbose_name_plural = '部门表'

# 班组
class ClassModel(models.Model):
    # 名称
    name = models.CharField(max_length=20,verbose_name ='名称')
    # 描述
    description = models.TextField(blank=True,verbose_name ='描述')
    # 所属部门
    group = models.ForeignKey(GroupModel, on_delete=models.DO_NOTHING,verbose_name ='所属部门')
    # 创建时间
    crtime = models.DateTimeField(auto_now_add=True,verbose_name ='创建时间')
    # 修改时间
    uptime = models.DateTimeField(auto_now=True,verbose_name ='修改时间')
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['crtime']
        verbose_name = '班组表'
        verbose_name_plural = '班组表'
# 职务
class OfficeModel(models.Model):
    # 职务名称
    name = models.CharField(max_length=20,verbose_name ='名称')
    # 描述
    description = models.TextField(blank=True,verbose_name ='描述')
    # 所属部门id
    groupid = models.ForeignKey(GroupModel, on_delete=models.DO_NOTHING,blank=True,verbose_name ='所属部门')
    # 所属班组id
    classid = models.ForeignKey(ClassModel, on_delete=models.DO_NOTHING,blank=True,verbose_name ='所属班组')
    # 创建时间
    crtime = models.DateTimeField(auto_now_add=True,verbose_name ='创建时间')
    # 修改时间
    uptime = models.DateTimeField(auto_now=True,verbose_name ='修改时间')
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['crtime']
        verbose_name = '职务表'
        verbose_name_plural = '职务表'

# 人员信息
class PersonnelModel(models.Model):
    # 用户id
    uid = models.OneToOneField(User, on_delete=models.DO_NOTHING,verbose_name ='用户id')
    # 昵称
    nickname = models.CharField(max_length=20, verbose_name='昵称')
    # 职工编号
    numid = models.CharField(max_length=20, verbose_name='职工编号')
    # 手机号码
    phonenum = models.CharField(max_length=20, verbose_name='手机号码')
    # 办公电话
    phoneoffice = models.CharField(max_length=20, blank=True,verbose_name='办公电话')
    # 描述
    description = models.TextField(blank=True,verbose_name ='描述')
    # 所属部门id
    groupid = models.ForeignKey(GroupModel, on_delete=models.DO_NOTHING,blank=True,null=True,verbose_name ='所属部门')
    # 所属班组id
    classid = models.ForeignKey(ClassModel, on_delete=models.DO_NOTHING,blank=True,null=True,verbose_name ='所属班组')
    # 职务
    office = models.ManyToManyField(OfficeModel,blank=True,verbose_name ='职务')
    # 创建时间
    crtime = models.DateTimeField(auto_now_add=True,verbose_name ='创建时间')
    # 修改时间
    uptime = models.DateTimeField(auto_now=True,verbose_name ='修改时间')
    def __str__(self):
        return self.nickname
    class Meta:
        ordering = ['crtime']
        verbose_name = '职工信息'
        verbose_name_plural = '职工表'
