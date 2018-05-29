# coding=utf-8
from django.conf import settings
from django.db import models


class CourseCategory(models.Model):
    name = models.CharField("课程类目", max_length=200, unique=True)
    intro = models.CharField("类目介绍", max_length=500, blank=True)
    ctime = models.DateTimeField(auto_now_add=True)
    utime = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'course_category'
        verbose_name = '课程类目'
        verbose_name_plural = '课程类目'

    def __str__(self):
        return self.name


LEVEL_TYPE_CHOICES = (
    (0, "入门"),
    (1, "基础"),
    (2, "进阶"),
    (3, "高级"),
    (4, "顶级"),
)

PUBLIC_TYPE_CHOICES = (
    (0, "公开课"),
    (1, "系统课"),
)


class Course(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
                             on_delete=models.SET_NULL)
    category = models.ForeignKey(CourseCategory, null=True,
                                 on_delete=models.SET_NULL)
    title = models.CharField("课程标题", max_length=200)
    cover = models.ImageField("课程封面", upload_to="course/cover", blank=True)
    price = models.FloatField("课程价格", default=999)
    level = models.SmallIntegerField("课程级别", default=0,
                                     choices=LEVEL_TYPE_CHOICES)
    public_type = models.SmallIntegerField("课程类型", default=0,
                                           choices=PUBLIC_TYPE_CHOICES)
    intro = models.CharField("课程介绍", max_length=1000)
    notice = models.TextField("听课须知", blank=True)
    ctime = models.DateTimeField(auto_now_add=True)
    utime = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'courses'
        verbose_name = '在线课程'
        verbose_name_plural = '在线课程'

    def __str__(self):
        return self.title
    

class CourseChapter(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    title = models.CharField("章节标题", max_length=200, blank=True)
    index = models.SmallIntegerField("章节顺序", default=0)
    notebook = models.FileField("notebook文件", max_length=500, blank=True)
    video = models.FileField("视频文件", max_length=500, blank=True)
    ppt = models.FileField("PPT文件", max_length=500, blank=True)
    url = models.CharField("内容地址", max_length=500, blank=True,
                           help_text="非notebook类型，自建地址")
    approve = models.IntegerField("点赞数", default=0)
    ctime = models.DateTimeField(auto_now_add=True)
    utime = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'course_chapter'
        verbose_name = '课程章节'
        verbose_name_plural = '课程章节'

    def __str__(self):
        return self.title


class ChapterComment(models.Model):
    course_chapter = models.ForeignKey(CourseChapter, null=True,
                                       on_delete=models.SET_NULL)
    comment = models.CharField("评论内容", max_length=500, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
                             on_delete=models.SET_NULL)
    parent = models.ForeignKey("self", null=True, blank=True,
                               on_delete=models.SET_NULL)
    ctime = models.DateTimeField(auto_now_add=True)
    utime = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'course_comment'
        verbose_name = '课程评论'
        verbose_name_plural = '课程评论'
    
    def __str__(self):
        return self.comment
