from django.contrib import admin
from .models import task, comment

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'creator')
    list_display_links = ('title',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    list_display_links = ('id', 'user')

admin.site.register(task, TaskAdmin)
admin.site.register(comment, CommentAdmin)
