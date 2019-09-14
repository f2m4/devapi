from django.contrib import admin
from .models import QingGongModel,TagModel
# Register your models here.

#工作定额
@admin.register(QingGongModel)
class QingGongAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'workingHours','fee', 'remark','crtime', 'uptime')\

#定额标签
@admin.register(TagModel)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'descript','crtime', 'uptime')