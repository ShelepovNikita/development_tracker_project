from django.contrib import admin
from selections.models import Selection


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


admin.site.register(Selection, SelectionAdmin)
