from django.contrib import admin
from kww_app.models import ProjectCompany, Company, CompanyType, Country


class ProjectCompanyInline(admin.TabularInline):
    model = ProjectCompany
    extra = 1


#class CoutryInline(admin.TabularInline):
#    model = Country
#    extra = 1


class CompanyAdmin(admin.ModelAdmin):
    inlines = [ProjectCompanyInline, ]#TechnologyUseInline, ]


admin.site.register(Company, CompanyAdmin)
admin.site.register(CompanyType)
admin.site.register(Country)