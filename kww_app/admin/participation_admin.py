from django.contrib import admin
from kww_app.models import ProjectParticipation, ProjectParticipationIssue, TechnologyUse, TechnologieIssue


class ProjectParticipationInline(admin.TabularInline):
    model = ProjectParticipation
    extra = 0


class ProjectParticipationIssueInline(admin.TabularInline):
    model = ProjectParticipationIssue
    extra = 0


class TechnologyUseInline(admin.TabularInline):
    model = TechnologyUse
    extra = 0


class ProjectParticipationAdmin(admin.ModelAdmin):
    inlines = [ProjectParticipationIssueInline, TechnologyUseInline]


admin.site.register(ProjectParticipation, ProjectParticipationAdmin)