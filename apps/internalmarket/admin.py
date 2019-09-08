from django.contrib import admin
from .models import QingGongModel
# Register your models here.


@admin.register(QingGongModel)
class QingGongAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'workingHours','fee', 'remark','crtime', 'uptime')