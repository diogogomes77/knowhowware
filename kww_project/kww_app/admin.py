from django.contrib import admin

from kww_app.models import Project, Participant, ProjectParticipation, Role


class ProjectParticipationInline(admin.TabularInline):
    model = ProjectParticipation
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectParticipationInline, ]


admin.site.register(Project, ProjectAdmin)


class ParticipantAdmin(admin.ModelAdmin):
    inlines = [ProjectParticipationInline, ]


admin.site.register(Participant, ParticipantAdmin)


class RolesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Role, RolesAdmin)