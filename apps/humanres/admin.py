from django.contrib import admin
from . import models
# Register your models here.

# 页面标题
admin.site.site_title="设备数据管理"
# 登录页导航条和首页导航条标题
admin.site.site_header="轻合金生产保障中心后台"
# 主页标题
admin.site.index_title="欢迎登陆"


@admin.register(models.GroupModel)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'crtime', 'uptime')
    # site_header = '设备管理系统'  # 此处设置页面显示标题
    # site_title = '设备管理'  # 此处设置页面头部标题


@admin.register(models.ClassModel)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description','group', 'crtime', 'uptime')

@admin.register(models.OfficeModel)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ('id', 'uid', 'description', 'groupid','classid','crtime', 'uptime')
