from django.shortcuts import render, get_object_or_404
from tasks.models import task
from users.models import User
from django.views.generic import (
     ListView,
     DetailView
)
from .choices import assignee_choices, priority_choices, progress_choices


class TaskListView(ListView):
    model = task
    template_name = 'pages/index.html'
    context_object_name = 'jobs'
    ordering = ['-date_created']
    extra_context = {
        'assignee_choices': assignee_choices,
        'progress_choices': progress_choices,
        'priority_choices': priority_choices 
    }


class TaskDetailView(DetailView):
      model = task
      template_name = 'pages/task_detail.html'
      context_object_name = 'post'

def search(request):
    queryset_list = task.objects.order_by('-date_created')


    if 'priority' in request.GET:
        priority = request.GET['priority']
        if priority:
            queryset_list = queryset_list.filter(priority__iexact=priority)

    if 'progress' in request.GET:
        progress = request.GET['progress']
        if progress:
            queryset_list = queryset_list.filter(progress__iexact=progress)
    
    if 'assignee' in request.GET:
        queryset_updated_list = []
        assignee_username = request.GET['assignee']
        if assignee_username:
            assignee = get_object_or_404(User, username=assignee_username)
            for query in queryset_list:
                if assignee in query.assignees.all():
                    queryset_updated_list.append(query)
        queryset_list = queryset_updated_list
    context = {
        'results': queryset_list
    }
    return render(request, 'pages/search.html', context)

def about(request):
    return render(request, 'pages/about.html')