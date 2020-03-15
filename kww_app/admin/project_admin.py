from django.contrib import admin

from kww_app.admin.participation_admin import ProjectParticipationInline
from kww_app.admin.technology_admin import TechnologyUseInline
from kww_app.models import Project


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectParticipationInline, ]#TechnologyUseInline, ]


admin.site.register(Project, ProjectAdmin)

