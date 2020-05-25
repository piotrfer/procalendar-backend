from django.urls import path, include
from .views import *

urlpatterns = [
    path('', EventsListView.as_view())
]
