from django.contrib import admin
from kww_app.models import ProjectParticipation, ProjectParticipationIssue, TechnologyUse


class ProjectParticipationInline(admin.TabularInline):
    model = ProjectParticipation
    extra = 1


class ProjectParticipationIssueInline(admin.TabularInline):
    model = ProjectParticipationIssue
    extra = 1


class TechnologyUseInline(admin.TabularInline):
    model = TechnologyUse
    extra = 1


class ProjectParticipationAdmin(admin.ModelAdmin):
    inlines = [ProjectParticipationIssueInline, TechnologyUseInline]


admin.site.register(ProjectParticipation, ProjectParticipationAdmin)