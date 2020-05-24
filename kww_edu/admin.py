from django.contrib import admin

from kww_edu.models import Institution, Course, Module, Student, HadCourse


class CourseInline(admin.TabularInline):
    model = Course
    extra = 1


class ModuleInline(admin.TabularInline):
    model = Module
    extra = 1


class InstitutionAdmin(admin.ModelAdmin):
    inlines = [CourseInline]


class CourseAdmin(admin.ModelAdmin):
    inlines = [ModuleInline]


class ModuleAdmin(admin.ModelAdmin):
   pass


class HadCourseInline(admin.TabularInline):
    model = HadCourse
    extra = 1


class StudentAdmin(admin.ModelAdmin):
   inlines = [HadCourseInline,]


admin.site.register(Institution, InstitutionAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Student, StudentAdmin)