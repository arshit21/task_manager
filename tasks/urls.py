from django.urls import path
from .views import TaskDetailView, create_task

urlpatterns = [
    path('<int:pk>',TaskDetailView, name='task-detail'),
    path('create_task/', create_task, name='create_task')
]