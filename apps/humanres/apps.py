from django.apps import AppConfig


class HumanresConfig(AppConfig):
    name = 'humanres'
    # 设置后台显示的app名称。需要在init内导入一下。
    verbose_name='HR管理'
