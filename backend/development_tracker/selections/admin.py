from django.contrib import admin
from .models import Selection


class SelectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'imageHover',)  # Отображаемые поля в списке объектов Selection
    search_fields = ('name', 'description', 'imageHover',)  # Поля для поиска в админ-панели
    # Остальные настройки, если необходимо


admin.site.register(Selection, SelectionAdmin)
