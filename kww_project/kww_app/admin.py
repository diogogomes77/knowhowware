from django.contrib import admin

from kww_app.models import Project, Participant, ProjectParticipation, Role, Technology, TechnologyUse, \
    ProjectParticipationIssue


class ProjectParticipationInline(admin.TabularInline):
    model = ProjectParticipation
    extra = 1


class TechnologyUseInline(admin.TabularInline):
    model = TechnologyUse
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectParticipationInline, TechnologyUseInline, ]


admin.site.register(Project, ProjectAdmin)


class ParticipantAdmin(admin.ModelAdmin):
    inlines = [ProjectParticipationInline, TechnologyUseInline, ]


admin.site.register(Participant, ParticipantAdmin)


class RolesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Role, RolesAdmin)


class TechnologyAdmin(admin.ModelAdmin):
    inlines = [TechnologyUseInline, ]


admin.site.register(Technology, TechnologyAdmin)


class ProjectParticipationIssueInline(admin.TabularInline):
    model = ProjectParticipationIssue
    extra = 1


class ProjectParticipationAdmin(admin.ModelAdmin):
    inlines = [ProjectParticipationIssueInline, ]


admin.site.register(ProjectParticipation, ProjectParticipationAdmin)