from django.contrib import admin
from kww_app.admin.participation_admin import ProjectParticipationInline
from kww_app.models import Project, ProjectType, ProjectCompany


class ProjectCompanyInline(admin.TabularInline):
    model = ProjectCompany
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectParticipationInline, ProjectCompanyInline, ]


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectType)

