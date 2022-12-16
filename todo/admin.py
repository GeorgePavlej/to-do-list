from django.contrib import admin

from todo.models import Task, Tag


admin.site.register(Tag)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ("content",)
    list_filter = ("tags",)