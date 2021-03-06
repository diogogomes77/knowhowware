from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.contenttypes.admin import GenericTabularInline

from kww_app.admin.participation_admin import ProjectParticipationInline
from kww_app.admin.technology_admin import TechnologyUseInline
from kww_app.models import Participant, Role, HasJob, Link


class LinksInline(GenericTabularInline):
    model = Link
    ct_fk_field = "object_id"
    ct_field = "content_type"
    extra = 1


class HasJobInline(admin.TabularInline):
    model = HasJob
    extra = 1


class ParticipantAdmin(UserAdmin):
    inlines = [ProjectParticipationInline, HasJobInline, LinksInline]#TechnologyUseInline, ]

    list_display = (
        'username',
        'email',
    )

    fieldsets = (
        ('Credentials', {
            'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('email',)}),
    )
    add_fieldsets = (
        ('Credentials', {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'), }),
        (('Personal info'), {'fields': ('email',)}),
    )

    def get_inlines(self, request, obj):
        if obj:
           return self.inlines
        return []


admin.site.register(Participant, ParticipantAdmin)


class RolesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Role, RolesAdmin)


