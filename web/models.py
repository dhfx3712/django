from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.utils.html import format_html    # 个人理解就是将format_html后跟的字符串以HTML输出


class Student(models.Model):
    """
    学员信息 [表定义，相关一些操作]
    """
    studentName = models.CharField('学员姓名', max_length=255)
    studentAge = models.IntegerField('学员年龄', null=True, blank=True)

    class Meta:    # 这里是Django的用法，给model定义元数据
        verbose_name = '学员信息管理'  # 给模型类起个别名
        verbose_name_plural = '学员信息管理'  # 指定模型的复数形式是什么

    # 行级按钮/操作定义 -- 处理一条记录
    def alert(self):
        # 此处你想展示什么，就写什么html代码
        btn = '<input type="button" value="点我弹出" onclick="javascript:alert(\''+self.studentName+'\');"/>'
        # 返回一个html信息对象
        return format_html(btn)

    alert.short_description='操作'


    def __str__(self):   # 类中如果定义了__str__方法，print打印对象时就会输出这个函数返回的字符串
        return self.studentName


class Contact(models.Model):
    """
    联系方式表，和学生有关联
    """
    info = models.CharField('联系方式', max_length=16)
    Student = models.ForeignKey("Student", on_delete=models.CASCADE, verbose_name="学生信息")

    class Meta:
        verbose_name = '联系方式'
        verbose_name_plural = '联系方式列表' # 复数 -- 展示多个的时候

    def __str__(self):  # 类中如果定义了__str__方法，print打印对象时就会输出这个函数返回的字符串
        return ''


class ExamInfo(models.Model):
    """
    考试信息表
    """
    score = models.IntegerField('考试总分')
    remark = models.CharField('备注', max_length=16)
    Student = models.ForeignKey("Student", on_delete=models.CASCADE, verbose_name="学生信息")

    class Meta:
        verbose_name = '考试信息'
        verbose_name_plural = '考试信息列表' # 复数 -- 展示多个的时候

    def __str__(self):
        return ''


class ExamDetailInfo(models.Model):
    """
    考试信息详情表
    """
    score = models.IntegerField('分数')
    className = models.CharField('科目', max_length=16)
    ExamInfo = models.ForeignKey("ExamInfo", on_delete=models.CASCADE, verbose_name="考试记录")

    class Meta:
        verbose_name = '考试详情'
        verbose_name_plural = '考试详情' # 复数 -- 展示多个的时候

    def __str__(self):
        return ''