from django.urls import path
from .views import (
    about,
    TaskListView,
    search
)

urlpatterns = [
    path('', TaskListView.as_view(), name='index'),
    path('about/', about, name='about'),
    path('search/',search, name='search' )
]