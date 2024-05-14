from django.contrib import admin

from notes.models import NotesModel

# Register your models here.


class NotesAdmin(admin.ModelAdmin):
    fields = ("name", "text", "last_modified", "date_created")
    list_display = ["id", "name"]
    search_fields = ["name"]
    ordering = ("id", "name")
    readonly_fields = ("date_created", "last_modified")


admin.site.register(NotesModel, NotesAdmin)
