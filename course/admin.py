# coding=utf-8
from django.contrib import admin

from course.models import CourseCategory, Course, CourseChapter, ChapterComment


class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "intro", "ctime")


admin.site.register(CourseCategory, CourseCategoryAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "level", "price", "ctime")


admin.site.register(Course, CourseAdmin)


class CourseChapterAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "course", "index", "ctime")


admin.site.register(CourseChapter, CourseChapterAdmin)


class ChapterCommentAdmin(admin.ModelAdmin):
    list_display = ("id", "course_chapter", "comment", "user", "ctime")


admin.site.register(ChapterComment, ChapterCommentAdmin)
