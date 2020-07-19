from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from kww_app.admin.participation_admin import ProjectParticipationInline
from kww_app.models import Project, ProjectType, ProjectCompany, Link


class LinksInline(GenericTabularInline):
    model = Link
    ct_fk_field = "object_id"
    ct_field = "content_type"
    extra = 1


class ProjectCompanyInline(admin.TabularInline):
    model = ProjectCompany
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectParticipationInline, ProjectCompanyInline, LinksInline]
    #fields = ['image_tag']
    readonly_fields = ['image_tag']


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectType)

