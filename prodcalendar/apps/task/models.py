from django.db import models
from django.contrib.auth import get_user_model
from ..activity.models import Activity

class Task(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='tasks', null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    activity = models.ForeignKey(Activity, on_delete=models.DO_NOTHING)
    active = models.BooleanField(default=True)
