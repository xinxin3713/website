# Generated by Django 2.0.3 on 2018-03-31 16:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChapterComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(blank=True, max_length=500, verbose_name='评论内容')),
                ('ctime', models.DateTimeField(auto_now_add=True)),
                ('utime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '课程评论',
                'verbose_name_plural': '课程评论',
                'db_table': 'course_comment',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='课程标题')),
                ('cover', models.ImageField(blank=True, upload_to='course/cover', verbose_name='课程封面')),
                ('price', models.FloatField(default=0, verbose_name='课程价格')),
                ('level', models.SmallIntegerField(choices=[(0, '入门'), (1, '基础'), (2, '进阶'), (3, '高级'), (4, '顶级')], default=0, verbose_name='课程级别')),
                ('public_type', models.SmallIntegerField(choices=[(0, '公开课'), (1, '系统课')], default=0, verbose_name='课程类型')),
                ('intro', models.CharField(max_length=1000, verbose_name='课程介绍')),
                ('notice', models.TextField(blank=True, verbose_name='听课须知')),
                ('ctime', models.DateTimeField(auto_now_add=True)),
                ('utime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '在线课程',
                'verbose_name_plural': '在线课程',
                'db_table': 'courses',
            },
        ),
        migrations.CreateModel(
            name='CourseCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='课程类目')),
                ('intro', models.CharField(blank=True, max_length=500, verbose_name='类目介绍')),
                ('ctime', models.DateTimeField(auto_now_add=True)),
                ('utime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '课程类目',
                'verbose_name_plural': '课程类目',
                'db_table': 'course_category',
            },
        ),
        migrations.CreateModel(
            name='CourseChapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, verbose_name='章节标题')),
                ('index', models.SmallIntegerField(default=0, verbose_name='章节顺序')),
                ('notebook', models.FileField(blank=True, max_length=500, upload_to='', verbose_name='notebook文件')),
                ('video', models.FileField(blank=True, max_length=500, upload_to='', verbose_name='视频文件')),
                ('ppt', models.FileField(blank=True, max_length=500, upload_to='', verbose_name='PPT文件')),
                ('url', models.CharField(blank=True, help_text='非notebook类型，自建地址', max_length=500, verbose_name='内容地址')),
                ('approve', models.IntegerField(default=0, verbose_name='点赞数')),
                ('ctime', models.DateTimeField(auto_now_add=True)),
                ('utime', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.Course')),
            ],
            options={
                'verbose_name': '课程章节',
                'verbose_name_plural': '课程章节',
                'db_table': 'course_chapter',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.CourseCategory'),
        ),
        migrations.AddField(
            model_name='course',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chaptercomment',
            name='course_chapter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.CourseChapter'),
        ),
        migrations.AddField(
            model_name='chaptercomment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.ChapterComment'),
        ),
        migrations.AddField(
            model_name='chaptercomment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
