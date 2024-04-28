from django.contrib import admin

from notes.models import NotesModel

# Register your models here.


class NotesAdmin(admin.ModelAdmin):
    fields = ("name", "text")
    list_display = ["id", "name"]
    search_fields = ["name"]
    ordering = ("id", "name")


admin.site.register(NotesModel, NotesAdmin)
