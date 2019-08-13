from django.apps import AppConfig


class SpmanageConfig(AppConfig):
    name = 'spmanage'
    # 设置后台显示的app名称。需要在init内导入一下。
    verbose_name='备件管理'