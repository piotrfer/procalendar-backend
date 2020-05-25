from django.urls import path, include
from .views import *

urlpatterns = [
    path('', ActivitiesListView.as_view())
]
