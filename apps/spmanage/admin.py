from django.contrib import admin
from . import models

#厂家信息
@admin.register(models.FactoryModel)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'addr', 'contactname', 'phone', 'crtime', 'uptime')

# 备件类型
@admin.register(models.TypeModel)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'crtime', 'uptime')

# 备件信息
@admin.register(models.InfoModel)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'typenum', 'factoryid', 'typeid', 'crtime', 'uptime')

# 入库表
@admin.register(models.InlabModel)
class InlabAdmin(admin.ModelAdmin):
    list_display = ('id', 'infoid', 'num', 'unitprice', 'userid', 'addr', 'remark','crtime', 'uptime')

# 出库表
@admin.register(models.OutlabModel)
class OutlabAdmin(admin.ModelAdmin):
    list_display = ('id', 'inlabid', 'num', 'userid', 'remark', 'crtime', 'uptime')