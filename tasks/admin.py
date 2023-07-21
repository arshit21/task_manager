from django.contrib import admin
from .models import task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'creator')
    list_display_links = ('title',)

admin.site.register(task, TaskAdmin)

