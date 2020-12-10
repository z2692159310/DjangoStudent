# @Time : 2020/12/10 21:37 
# @Author : 小四先生
# @File : adminx.py
# @Version : 1.0
# @Description : xadmin数据模型
import xadmin

from xadmin import views

from DjangoStudent.models import Students, Class, Subjects, Teachers


# 主题设置
class BaseSetting(object):
    # 后台的主题功能，xadmin默认是关掉的，所以要打开
    enable_themes = True
    use_bootswatch = True


# 全局设置
class GlobalSetting(object):
    # 设置base_site.html的Title(页头名称)
    site_title = 'Mr.小四'

    # 设置base_site.html的Footer(页脚)
    site_footer = 'Mr.小四'

    # 设置菜单折叠
    menu_style = "accordion"


# Student显示设置
class StudentsAdmin(object):
    # 列表中显示的字段
    list_display = ('id', 'name', 'sex', 'age', 'address', 'enter_date', 'remarks')

    # 内联复选框(选课系统可以多选)
    style_fields = {'subjects': 'checkbox-inline', }

    # 搜索(姓名, 班级, 课程)
    search_fields = ('name', 'class_name__class_name', 'subjects__name',)

    # 过滤器(按性别)
    list_filter = ('sex',)

    # # 顺序排序
    # ordering = ('age', 'name',)
    # # 逆序排序，在前面加一个减号"-"，例如按年龄倒序排列
    # ordering = ('-age',)

    # 显示数据详情
    # show_detail_fields = ['name']


# Class显示设置
class ClassAdmin(object):
    # 列表中显示的字段
    list_display = ('class_name',)


# Subject显示设置
class SubjectsAdmin(object):
    # 列表中显示的字段
    list_display = ('name', 'score',)


# Teachers显示设置
class TeachersAdmin(object):
    # 列表中显示的字段
    list_display = ('name',)


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)

xadmin.site.register(Students, StudentsAdmin)
xadmin.site.register(Class, ClassAdmin)
xadmin.site.register(Subjects, SubjectsAdmin)
xadmin.site.register(Teachers, TeachersAdmin)
