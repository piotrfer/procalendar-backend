from django.urls import path, include
from .views import WeekView

urlpatterns = [
    path('show/', WeekView.as_view()),
]