from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from tasks.models import task
from .models import User


def register(request, *args, **kwargs):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			form.save()
			messages.success(request, f'Your Account has been created! You are now able to log in')
			return redirect('index')

	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html',{'form': form})

class UserTaskListView(ListView):
	model = task
	template_name = 'users/user_task.html'
	context_object_name = 'jobs'
	ordering = ['-date_created']
	paginate_by = 4

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return task.objects.filter(creator=user).order_by('-date_created')

@login_required
def profile(request):
	tasks = task.objects.order_by('-date_created')
	user_tasks = []
	user = request.user
	for Task in tasks:
		if user in Task.assignees.all():
			user_tasks.append(Task)


	context = {
		'tasks': user_tasks
	}
	return render(request, 'users/profile.html', context)