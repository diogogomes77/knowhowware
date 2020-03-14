from django.contrib import admin

from kww_app.admin.participation_admin import ProjectParticipationInline
from kww_app.admin.technology_admin import TechnologyUseInline
from kww_app.models import Participant, Role


class ParticipantAdmin(admin.ModelAdmin):
    inlines = [ProjectParticipationInline, TechnologyUseInline, ]


admin.site.register(Participant, ParticipantAdmin)


class RolesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Role, RolesAdmin)