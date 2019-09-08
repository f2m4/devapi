from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from . import models

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
    list_display = ('id', 'name', 'description', 'groupid','classid','crtime', 'uptime')\


@admin.register(models.PersonnelModel)
class PersonnelAdmin(admin.ModelAdmin):
    list_display = ('id', 'uid','nickname','numid','phonenum', 'phoneoffice','description', 'groupid','classid','office_list','crtime', 'uptime')

    # 多对多关系
    def office_list(self, obj):
        """自定义列表字段"""
        office_names = map(lambda x: x.name, obj.office.all())
        return ', '.join(office_names)



# # 自定义行内类
# class PersonnelInline(admin.StackedInline):
#     model = models.PersonnelModel
#     can_delete = False
#     verbose_name_plural = '职工信息'
#
# # Define a new User admin
# class UserAdmin(BaseUserAdmin):
#     inlines = (PersonnelInline,)
#     list_display = ('username', 'nickname','email', 'first_name', 'last_name', 'is_staff')
#
#     def nickname(self,obj):
#         return obj.personnelmodel.nickname
#     nickname.short_description = '昵称'
# # Re-register UserAdmin
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)