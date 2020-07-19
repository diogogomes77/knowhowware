from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from kww_app.models import ProjectCompany, Company, CompanyType, Country, Link


class LinksInline(GenericTabularInline):
    model = Link
    ct_fk_field = "object_id"
    ct_field = "content_type"
    extra = 1


class ProjectCompanyInline(admin.TabularInline):
    model = ProjectCompany
    extra = 1


#class CoutryInline(admin.TabularInline):
#    model = Country
#    extra = 1


class CompanyAdmin(admin.ModelAdmin):
    inlines = [ProjectCompanyInline, LinksInline]#TechnologyUseInline, ]


admin.site.register(Company, CompanyAdmin)
admin.site.register(CompanyType)
admin.site.register(Country)