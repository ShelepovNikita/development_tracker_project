from django.contrib import admin

from selections.models import Selection, SelectionSkill


class SelectionAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "imageHover",
    )
    search_fields = (
        "name",
        "description",
        "imageHover",
    )


class SelectionSkillAdmin(admin.ModelAdmin):
    list_display = (
        "selection",
        "skill",
    )
    search_fields = (
        "selection",
        "skill",
    )


admin.site.register(Selection, SelectionAdmin)
admin.site.register(SelectionSkill, SelectionSkillAdmin)
