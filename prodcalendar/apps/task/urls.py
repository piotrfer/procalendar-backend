from django.urls import path, include
from .views import *

urlpatterns = [
    path('', TasksListView.as_view()),
    path('<int:id>', TaskDetailView.as_view())
]
