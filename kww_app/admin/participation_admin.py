from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from kww_app.models import ProjectParticipation, ProjectParticipationIssue, TechnologyUse, TechnologieIssue, Link


class LinksInline(GenericTabularInline):
    model = Link
    ct_fk_field = "object_id"
    ct_field = "content_type"
    extra = 1


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
    inlines = [ProjectParticipationIssueInline, TechnologyUseInline, LinksInline]


admin.site.register(ProjectParticipation, ProjectParticipationAdmin)