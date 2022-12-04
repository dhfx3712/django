from django.contrib import admin

# Register your models here.
import nested_admin
from django.contrib import admin

# Register your models here.
from .models import Student, Contact, ExamInfo, ExamDetailInfo


# TabularInline 表格形式的展示，一行一行
class ContactAdmin(nested_admin.NestedTabularInline):  # 联系方式
    # 指定要展示哪些内容
    list_display = ['id', 'info']
    model = Contact
    extra = 0  # 表格默认展示几行


class ExamDetailInfoAdmin(nested_admin.NestedTabularInline):   # 考试详情
    model = ExamDetailInfo
    extra = 0  # 表格默认展示几行


# NestedStackedInline 【上下排版】
class ExamInfoAdmin(nested_admin.NestedStackedInline):      # 考试信息
    model = ExamInfo
    extra = 0  # 表格默认展示几行
    inlines = [ExamDetailInfoAdmin]


# ModelAdmin 常规展示【上下排版】
class StudentAdmin(nested_admin.NestedModelAdmin):     # 学员信息管理
    """
    学员信息
    """
    # 指定要展示哪些内容
    list_display = ['id', 'studentName', 'studentAge', 'alert']
    model = Student
    inlines = [ContactAdmin, ExamInfoAdmin] #-- 嵌套一个 联系方式的维护页面

    actions = ['test_btn']  # 按钮定义

    @admin.action(permissions=['change'])  # 权限定义
    def test_btn(self, httprequest, queryset):
        # 此处可以进行数据库操作等等...
        print('请求信息：', httprequest)
        print('页面选择的数据信息：', queryset)
        self.message_user(httprequest, '执行成功')  # 弹出一个对话框给前端提示

    test_btn.short_description = '执行测试用例'
    test_btn.confirm = '这是一个对话框，你确定要执行这个按钮的动作嘛？'

admin.site.register(Student, StudentAdmin)
# admin.site.register(Contact, ContactAdmin) # 此页面已经被嵌套在学生信息界面，不需要独立成为一个页面了