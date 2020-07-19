from django.contrib import admin
from kww_app.models import LinkType


class LinkTypeAdmin(admin.ModelAdmin):
    pass


admin.site.register(LinkType, LinkTypeAdmin)
