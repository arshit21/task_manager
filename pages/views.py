from django.shortcuts import render, get_object_or_404
from tasks.models import task
from users.models import User
from django.views.generic import (
     ListView,
     DetailView
)
from .choices import assignee_choices, priority_choices, progress_choices, due_date_choices
from datetime import datetime
from dateutil.relativedelta import relativedelta
from pytz import timezone
from django.http import JsonResponse



class TaskListView(ListView):
    """Imports all models to display on home page"""
    model = task
    template_name = 'pages/index.html'
    context_object_name = 'jobs'
    ordering = ['-date_created']
    extra_context = {
        'assignee_choices': assignee_choices,
        'progress_choices': progress_choices,
        'priority_choices': priority_choices,
        'due_date_choices': due_date_choices,
    }


class TaskDetailView(DetailView):
      """Displays a specific model details"""
      model = task
      template_name = 'pages/task_detail.html'
      context_object_name = 'post'

def search(request):
    """View for searching objects"""
    queryset_list = task.objects.order_by('-date_created')


    if 'priority' in request.GET:
        """Search by priority"""
        priority = request.GET['priority']
        queryset_list = queryset_list.filter(priority__iexact=priority)

    if 'progress' in request.GET:
        """Search by progress"""
        progress = request.GET['progress']
        queryset_list = queryset_list.filter(progress__iexact=progress)
    
    if 'due_date_duration' in request.GET:
        """Filter by due date"""
        queryset_updated_list = []
        due_date_duration = request.GET['due_date_duration']
        due_date_duration = int(due_date_duration)
        date_today = datetime.now(timezone('UTC'))
        due_date_filter = datetime.now(timezone('UTC')) + relativedelta(months=+due_date_duration)
        for query in queryset_list:
            query_due_date = query.due_date
            if(query_due_date < due_date_filter and query_due_date > date_today):
                queryset_updated_list.append(query)
        queryset_list = queryset_updated_list



    if 'assignee' in request.GET:
        """Search by assignee"""
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
    """about page"""
    return render(request, 'pages/about.html')