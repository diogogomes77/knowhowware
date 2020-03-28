from django.contrib import admin
from kww_app.models import Technology, TechnologyUse


class TechnologyUseInline(admin.TabularInline):
    model = TechnologyUse
    extra = 1


class TechnologyAdmin(admin.ModelAdmin):
    inlines = [TechnologyUseInline,]


admin.site.register(Technology, TechnologyAdmin)
