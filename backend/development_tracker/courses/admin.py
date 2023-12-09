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


admin.site.register(Course, CourseAdmin)
admin.site.register(CourseDefaultSkill)
