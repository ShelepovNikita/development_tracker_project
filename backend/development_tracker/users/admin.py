from django.contrib import admin

from users.models import CustomUser, UserSkill


class UserSkillAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "skill",
        "rate",
        "notes",
        "editable",
    )
    search_fields = (
        "user",
        "skill",
    )


admin.site.register(CustomUser)
admin.site.register(UserSkill, UserSkillAdmin)
