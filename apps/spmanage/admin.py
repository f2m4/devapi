from django.contrib import admin
from . import models

#厂家信息
@admin.register(models.FactoryModel)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'addr', 'contactname', 'phone', 'crtime', 'uptime')

# 备件类型
@admin.register(models.TypeModel)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'description', 'crtime', 'uptime')


# 备件信息
@admin.register(models.InfoModel)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('id',  'worklineid','name', 'description', 'typenum', 'factoryid', 'typeid')
    #设置点击进入编辑界面的链接字段
    list_display_links = ('id','name')
    #设置默认可编辑字段，在列表里就可以编辑  注意:不能与list_display_links重复
    list_editable = []
    #搜索框  字段
    search_fields=['worklineid', 'name','factoryid']
    #过滤字段
    list_filter = ['worklineid', 'typeid','factoryid']
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50


# 入库表
@admin.register(models.InlabModel)
class InlabAdmin(admin.ModelAdmin):
    list_display = ('id', 'infoid', 'num', 'unitprice', 'userid', 'addr', 'remark','crtime', 'uptime')

# 出库表
@admin.register(models.OutlabModel)
class OutlabAdmin(admin.ModelAdmin):
    list_display = ('id', 'inlabid', 'num', 'userid', 'remark', 'crtime', 'uptime')