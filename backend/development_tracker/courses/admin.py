from django.contrib import admin
from .models import Course, Skill, CourseDefaultSkill


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'url',)  # Отображаемые поля в списке
    search_fields = ('name', 'url',)  # Поля, по которым можно осуществлять поиск
    filter_horizontal = ('skills',)  # Добавление возможности выбора навыков в горизонтальном виде


admin.site.register(Course, CourseAdmin)
admin.site.register(Skill)
admin.site.register(CourseDefaultSkill)
