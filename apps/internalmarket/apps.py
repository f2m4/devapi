from django.apps import AppConfig


class InternalmarketConfig(AppConfig):
    name = 'internalmarket'
    # 设置后台显示的app名称。需要在init内导入一下。
    verbose_name='内部市场'
