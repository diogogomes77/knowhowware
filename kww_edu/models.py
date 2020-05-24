from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models


class Institution(models.Model):
    name = models.CharField(max_length=16)
    full_name = models.CharField(max_length=128, null=True, blank=True)
    city = models.CharField(max_length=64)
    country = models.CharField(max_length=32)
    website = models.URLField(max_length=256, null=True, blank=True)
    description = RichTextField(config_name='example', null=True, blank=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=128)
    institution = models.ForeignKey('Institution', on_delete=models.CASCADE, null=True)
    degree = models.CharField(max_length=64)
    description = RichTextField(config_name='example', null=True, blank=True)

    def __str__(self):
        return self.name

class Module(models.Model):
    name = models.CharField(max_length=128)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, null=True)
    description = RichTextField(config_name='example', null=True, blank=True)

    def __str__(self):
        return self.name


class HadModule(models.Model):
    module = models.ForeignKey('Module', on_delete=models.CASCADE)
    hadcourse = models.ForeignKey('HadCourse', on_delete=models.CASCADE)
    started_at = models.DateField()
    ended_at = models.DateField()
    grade = models.IntegerField()


class HadCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    started_at = models.DateField()
    ended_at = models.DateField()
    grade = models.IntegerField()
    modules = models.ManyToManyField(
        Module,
        through=HadModule,
        through_fields=('hadcourse', 'module'),
    )


class Student(models.Model):
    user = models.ForeignKey(User, related_name='student', on_delete=models.CASCADE)
    courses = models.ManyToManyField(
        Course,
        through=HadCourse,
        through_fields=('student', 'course')
    )

    def __str__(self):
        return self.user.username
