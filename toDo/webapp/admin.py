from django.contrib import admin

from webapp.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'status', 'deadline']
    search_fields = ['title', 'status']
    fields = ['id', 'title', 'description', 'deadline', 'status']
    readonly_fields = ['id']


admin.site.register(Task, TaskAdmin)
