from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import task
from users.models import User
from django.core.mail import send_mail
from .choices import assignee_choices, priority_choices, progress_choices

@login_required
def TaskDetailView(request, pk):
      post = get_object_or_404(task, id=pk)
      user=request.user
      if request.method == 'POST':
            progress = request.POST['progress']
            post.progress = progress
            post.save()

      context = {
            'post': post,
            'priority_choices': priority_choices,
            'progress_choices': progress_choices
      }
      return render(request, 'tasks/task_detail.html', context)

@login_required
def create_task(request):
      if request.method == 'POST':
            title = request.POST['title']
            description = request.POST['description']
            assignee_1_username = request.POST['assignee_1']
            assignee_2_username = request.POST['assignee_2']
            assignee_3_username = request.POST['assignee_3']
            priority = request.POST['priority']
            due_date = request.POST['due_date']
            labels = request.POST['labels']
            creator = request.user
            progress = 'Not Started'

            assignee_1 = get_object_or_404(User, username=assignee_1_username)
            assignee_2 = get_object_or_404(User, username=assignee_2_username)
            assignee_3 = get_object_or_404(User, username=assignee_3_username)
            
            Task = task.objects.create(creator_id=creator.id ,title=title, description=description, priority=priority, due_date=due_date, labels=labels, progress=progress)
            Task.assignees.add(assignee_1)
            Task.assignees.add(assignee_2)
            Task.assignees.add(assignee_3)
            Task.save()
            return redirect('index')
      context = {
            'assignee_choices': assignee_choices,
            'priority_choices': priority_choices
      }
      return render(request, 'tasks/create_task.html', context)