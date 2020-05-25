from django.urls import path, include
from .views import *

urlpatterns = [
    path('', ActivitiesListView.as_view()),
    path('<int:id>', ActivitiesDetailView.as_view()),
]
