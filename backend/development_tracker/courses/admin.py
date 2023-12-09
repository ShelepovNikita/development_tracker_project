from django.contrib import admin

from courses.models import Course, CourseDefaultSkill


class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "url",
    )
    search_fields = (
        "name",
        "url",
    )
    filter_horizontal = ("skills",)


class CourseDefaultSkillAdmin(admin.ModelAdmin):
    list_display = (
        "course",
        "skill",
    )
    search_fields = ("skill",)


admin.site.register(Course, CourseAdmin)
admin.site.register(CourseDefaultSkill, CourseDefaultSkillAdmin)
