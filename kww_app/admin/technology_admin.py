from django.contrib import admin
from kww_app.models import Technology, TechnologyUse, ParentTechnology


class TechnologyUseInline(admin.TabularInline):
    model = TechnologyUse
    extra = 1


class ParentTechologyInline(admin.TabularInline):
    model = ParentTechnology
    extra = 1
    fk_name = "parent"


class TechnologyAdmin(admin.ModelAdmin):
    inlines = [ParentTechologyInline, TechnologyUseInline,]


admin.site.register(Technology, TechnologyAdmin)
