from django.contrib import admin

from kww_app.models import Project, Participant, ProjectParticipation, Role, Technology, TechnologyUse, \
    ProjectParticipationIssue


class TechnologyUseInline(admin.TabularInline):
    model = TechnologyUse
    extra = 1


class TechnologyAdmin(admin.ModelAdmin):
    inlines = [TechnologyUseInline, ]


admin.site.register(Technology, TechnologyAdmin)
