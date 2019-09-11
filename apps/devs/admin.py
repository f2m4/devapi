from django.contrib import admin
from . import models
# Register your models here.

# 生产线
@admin.register(models.WorklineModel)
class WorklineAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description','groupid', 'crtime', 'uptime')
    #设置点击进入编辑界面的链接字段
    list_display_links = ('id', 'name')


# 设备
@admin.register(models.DevsModel)
class DevsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description','worklineid', 'crtime', 'uptime')
    #设置点击进入编辑界面的链接字段
    list_display_links = ('id', 'name')
    site_header = '设备管理系统'  # 此处设置页面显示标题
    site_title = '设备管理'  # 此处设置页面头部标题


# 设备包机人
@admin.register(models.MainmanModel)
class MainmanAdmin(admin.ModelAdmin):
    # 显示字段
    list_display = ('id', 'uid', 'description','inworkline','devsid_list', 'crtime', 'uptime')
    # 编辑字段
    fieldsets = (
        (None, {'fields': ('uid', 'description', 'devsid')}),
    )
    filter_horizontal = ('devsid',)
    #设置点击进入编辑界面的链接字段
    list_display_links = ('id', 'uid')
    #设置每页显示多少条记录，默认是100条
    list_per_page = 50

    # 定义devsid_list，方法名和devsid_list一致
    def devsid_list(self, obj):
        """自定义列表字段"""
        devs_names = map(lambda x: x.name, obj.devsid.all())
        return ', '.join(devs_names)
    # 定义列名
    devsid_list.short_description = '设备表'

    # 定义设备所属车间字段
    def inworkline(self,obj):
        workline_list = map(lambda x: x.worklineid.name, obj.devsid.all())
        workline_list=list(set(workline_list))
        return ', '.join(workline_list)
    # 定义列名
    inworkline.short_description = '所属车间'


    list_filter = ('uid', 'crtime') #过滤器
    # 可搜索名字，设备，生产线
    search_fields = ('uid__username', 'devsid__name','devsid__worklineid__name')          #搜索字段
    date_hierarchy = 'crtime'        #详细时间分层筛选

# 报修记录
@admin.register(models.DevRecordsModel)
class DevRecordsAdmin(admin.ModelAdmin):
    list_display = ('uid', 'devsid', 'description', 'level','crtime', 'uptime')
    #设置点击进入编辑界面的链接字段
    list_display_links = ('uid', 'description')

# 维修记录
@admin.register(models.WorkRecordsModel)
class WorkRecordsAdmin(admin.ModelAdmin):
    list_display = ('uid', 'devRecordid', 'description', 'isfininsh','crtime', 'uptime')
    #设置点击进入编辑界面的链接字段
    list_display_links = ('uid', 'description')


# 维修台帐
@admin.register(models.WorkRecModel)
class WorkRecAdmin(admin.ModelAdmin):
    list_display = ('id', 'devName', 'devPart', 'faultDescription','repairContent','workType','faultType',
                    'spareName','spareType','spareTypeId','spareUnit','spareQuantity','participants_list','description',
                    'isfininsh','recorder','bgTime','edTime','crtime', 'uptime')
    #设置点击进入编辑界面的链接字段
    list_display_links = ('id',)

    # 多对多自定义
    def participants_list(self, obj):
        """自定义列表字段"""
        participants_names = map(lambda x: x.first_name, obj.participants.all())
        return ', '.join(participants_names)
    # 定义列名
    participants_list.short_description = '参与人员'

# 时间测试
@admin.register(models.TTModel)
class TTAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'bir', 'crtime', 'uptime')
    #设置点击进入编辑界面的链接字段
    list_display_links = ('id', 'name')