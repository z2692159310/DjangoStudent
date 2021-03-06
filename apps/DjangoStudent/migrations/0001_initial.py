# Generated by Django 2.2 on 2020-12-10 13:41

import DjangoStudent.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=100, verbose_name='班级')),
            ],
            options={
                'verbose_name': '班级',
                'verbose_name_plural': '班级',
                'db_table': 't_class',
            },
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='课程名称')),
                ('score', models.IntegerField(blank=True, verbose_name='学分')),
            ],
            options={
                'verbose_name': '课程信息',
                'verbose_name_plural': '课程信息',
                'db_table': 't_subjects',
            },
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='教师姓名')),
            ],
            options={
                'verbose_name': '教师信息',
                'verbose_name_plural': '教师信息',
                'db_table': 't_teachers',
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='学生姓名')),
                ('photo', models.ImageField(blank=True, null=True, upload_to=DjangoStudent.models.Students.get_photo, verbose_name='照片')),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女')], max_length=50, verbose_name='性别')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('address', models.CharField(blank=True, max_length=250, verbose_name='家庭住址')),
                ('enter_date', models.DateField(verbose_name='入学时间')),
                ('remarks', models.TextField(blank=True, verbose_name='备注')),
                ('class_name', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='DjangoStudent.Class', verbose_name='所在班级')),
                ('subjects', models.ManyToManyField(blank=True, to='DjangoStudent.Subjects', verbose_name='选修课程')),
            ],
            options={
                'verbose_name': '学生信息',
                'verbose_name_plural': '学生信息',
                'db_table': 't_students',
            },
        ),
        migrations.AddField(
            model_name='class',
            name='headmaster',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DjangoStudent.Teachers', verbose_name='班主任'),
        ),
    ]
