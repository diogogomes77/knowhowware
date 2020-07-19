from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from kww_app.models import Technology, TechnologyUse, ParentTechnology, Link


class LinksInline(GenericTabularInline):
    model = Link
    ct_fk_field = "object_id"
    ct_field = "content_type"
    extra = 1


class TechnologyUseInline(admin.TabularInline):
    model = TechnologyUse
    extra = 1


class ParentTechologyInline(admin.TabularInline):
    model = ParentTechnology
    extra = 1
    fk_name = "parent"


class TechnologyAdmin(admin.ModelAdmin):
    inlines = [ParentTechologyInline, TechnologyUseInline, LinksInline]



admin.site.register(Technology, TechnologyAdmin)
