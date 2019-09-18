from django.contrib import admin
from .models import QingGongModel,TagModel
# Register your models here.

#工作定额
@admin.register(QingGongModel)
class QingGongAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'workingHours','fee', 'remark','crtime', 'uptime')
    # 设置点击进入编辑界面的链接字段
    list_display_links = ('id', 'name')
    # 设置默认可编辑字段，在列表里就可以编辑  注意:不能与list_display_links重复
    list_editable = []
    # 搜索框  字段
    search_fields = ['name']
    # 过滤字段
    # list_filter = ['workingHours', 'fee']
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50

#定额标签
@admin.register(TagModel)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'descript','crtime', 'uptime')
    # 设置点击进入编辑界面的链接字段
    list_display_links = ('id', 'name')
    # 设置默认可编辑字段，在列表里就可以编辑  注意:不能与list_display_links重复
    list_editable = []
    # 搜索框  字段
    search_fields = ['name']
    # 过滤字段
    # list_filter = ['name']
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50