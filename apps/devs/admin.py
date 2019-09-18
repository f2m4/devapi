from django.contrib import admin
from . import models
# Register your models here.

admin.site.site_header = '生产保障中心数据管理'
admin.site.site_title = '生产保障中心'


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
    #设置要显示在列表中的字段
    list_display = ('id', 'classId','devName', 'devPart', 'faultDescription','repairContent','workType','faultType',
                    'spareName','spareType','spareUnit','spareQuantity','participants_list','description',
                    'get_isfinish','recorder','bgTime','edTime','crtime')
    #设置点击进入编辑界面的链接字段
    list_display_links = ('id','faultDescription','repairContent')

    #设置默认可编辑字段，在列表里就可以编辑  注意:不能与list_display_links重复
    list_editable = []

    # 多对多自定义列
    def participants_list(self, obj):
        """自定义列表字段"""
        participants_names = map(lambda x: x.first_name, obj.participants.all())
        return ', '.join(participants_names)
    # 定义列名
    participants_list.short_description = '参与人员'

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50

    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-crtime',)

    #列表顶部，设置为False不在顶部显示，默认为True。
    actions_on_top=True

    #列表底部，设置为False不在底部显示，默认为False。
    actions_on_bottom=True

    #搜索框  字段
    search_fields=['devPart', 'faultDescription','repairContent']

    #过滤字段
    list_filter = ['classId']

    def get_isfinish(self, obj):
        if not obj.isfininsh:
            return "正在修复"
        else:
            return "完成"

    get_isfinish.short_description = '修复状态'
    get_isfinish.allow_tags = True
