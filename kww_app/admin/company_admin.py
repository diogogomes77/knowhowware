from django.contrib import admin

from kww_app.admin.participation_admin import ProjectParticipationInline
from kww_app.admin.technology_admin import TechnologyUseInline
from kww_app.models import Project, ProjectCompany, Company, CompanyType


class ProjectCompanyInline(admin.TabularInline):
    model = ProjectCompany
    extra = 1


class CompanyAdmin(admin.ModelAdmin):
    inlines = [ProjectCompanyInline, ]#TechnologyUseInline, ]


admin.site.register(Company, CompanyAdmin)
admin.site.register(CompanyType)
