from django.db import models
from users.models import User
from django.utils import timezone

class task(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator')
    title = models.CharField(max_length=255)
    description = models.TextField()
    assignees = models.ManyToManyField(User, related_name='assignee')
    due_date = models.DateTimeField()
    progress = models.CharField(max_length=20)
    priority = models.CharField(max_length=20)
    labels = models.CharField(max_length=100, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.creator.username

class comment(models.Model):
    task = models.ForeignKey(task, on_delete=models.CASCADE)
    comment = models.TextField()