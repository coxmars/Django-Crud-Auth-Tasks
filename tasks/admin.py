from django.contrib import admin
from .models import Task

# This class is used to customize the admin panel for the Task model to show the created field as read-only.
class TaskAdmin (admin.ModelAdmin):
    readonly_fields = ('created',)

# Register your models here.
admin.site.register(Task, TaskAdmin)