# Generated by Django 5.0.4 on 2024-10-26 07:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(choices=[('TOAN', 'Toán'), ('VAN', 'Ngữ Văn'), ('ANH', 'Tiếng Anh'), ('KHTN_HOA', 'Hoá'), ('KHTN_LY', 'Vật lý'), ('KHTN_SINH', 'Sinh học'), ('KHXH_DIA', 'Địa lý'), ('KHXH_SU', 'Lịch sử'), ('KHXH_GDCD', 'GDCD'), ('TD', 'Thể dục'), ('MT', 'Mỹ thuật'), ('AN', 'Âm nhạc'), ('TH', 'Tin học'), ('CN', 'Công nghệ'), ('HDTN-HN', 'Hoạt động trại nghiệm, hướng nghiệp')], max_length=20)),
                ('lesson_number', models.IntegerField(blank=True, null=True)),
                ('name_lesson', models.CharField(blank=True, max_length=100, null=True)),
                ('day', models.DateField()),
                ('comment', models.TextField(blank=True, null=True)),
                ('evaluate', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Lesson',
                'verbose_name_plural': 'Lessons',
            },
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('number', models.IntegerField(primary_key=True, serialize=False)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PlannedLesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(choices=[('TOAN', 'Toán'), ('VAN', 'Ngữ Văn'), ('ANH', 'Tiếng Anh'), ('KHTN_HOA', 'Hoá'), ('KHTN_LY', 'Vật lý'), ('KHTN_SINH', 'Sinh học'), ('KHXH_DIA', 'Địa lý'), ('KHXH_SU', 'Lịch sử'), ('KHXH_GDCD', 'GDCD'), ('TD', 'Thể dục'), ('MT', 'Mỹ thuật'), ('AN', 'Âm nhạc'), ('TH', 'Tin học'), ('CN', 'Công nghệ'), ('HDTN-HN', 'Hoạt động trại nghiệm, hướng nghiệp')], max_length=20)),
                ('lesson_number', models.IntegerField()),
                ('name_lesson', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Planned Lesson',
                'verbose_name_plural': 'Planned Lessons',
            },
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('name', models.IntegerField(primary_key=True, serialize=False)),
                ('day_begin', models.DateField()),
                ('number_of_weeks', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Semester',
                'verbose_name_plural': 'Semesters',
                'db_table': 'semester',
            },
        ),
        migrations.CreateModel(
            name='TeacherAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(choices=[('TOAN', 'Toán'), ('VAN', 'Ngữ Văn'), ('ANH', 'Tiếng Anh'), ('KHTN_HOA', 'Hoá'), ('KHTN_LY', 'Vật lý'), ('KHTN_SINH', 'Sinh học'), ('KHXH_DIA', 'Địa lý'), ('KHXH_SU', 'Lịch sử'), ('KHXH_GDCD', 'GDCD'), ('TD', 'Thể dục'), ('MT', 'Mỹ thuật'), ('AN', 'Âm nhạc'), ('TH', 'Tin học'), ('CN', 'Công nghệ'), ('HDTN-HN', 'Hoạt động trại nghiệm, hướng nghiệp')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(choices=[('TOAN', 'Toán'), ('VAN', 'Ngữ Văn'), ('ANH', 'Tiếng Anh'), ('KHTN_HOA', 'Hoá'), ('KHTN_LY', 'Vật lý'), ('KHTN_SINH', 'Sinh học'), ('KHXH_DIA', 'Địa lý'), ('KHXH_SU', 'Lịch sử'), ('KHXH_GDCD', 'GDCD'), ('TD', 'Thể dục'), ('MT', 'Mỹ thuật'), ('AN', 'Âm nhạc'), ('TH', 'Tin học'), ('CN', 'Công nghệ'), ('HDTN-HN', 'Hoạt động trại nghiệm, hướng nghiệp')], max_length=20)),
                ('score_type', models.CharField(choices=[('TX', 'Đánh giá thường xuyên'), ('GK', 'Điểm giữa kỳ'), ('CK', 'Điểm cuối kỳ')], max_length=10)),
                ('grade', models.FloatField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grades', to='accounts.student')),
            ],
            options={
                'verbose_name': 'Điểm',
                'verbose_name_plural': 'grades',
                'db_table': 'grades',
            },
        ),
    ]
