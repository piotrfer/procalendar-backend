from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('apps.authapp.urls')),
    path('activity/', include('apps.activity.urls')),
    path('event/', include('apps.event.urls')),
    path('task/', include('apps.task.urls')),
]
