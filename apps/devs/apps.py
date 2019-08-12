from django.apps import AppConfig


class DevsConfig(AppConfig):
    name = 'devs'
    # 设置后台显示的app名称。需要在init内导入一下。
    verbose_name='设备管理'
