from django.apps import AppConfig


class DjangostudentConfig(AppConfig):
    name = 'DjangoStudent'
    # 设置app标题 还需要在__init__中设置
    verbose_name = '学生管理系统'
