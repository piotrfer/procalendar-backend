from django.db import models
from django.contrib.auth import get_user_model
from ..activity.models import Activity

class Task(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='tasks', null=True)
    title = models.CharField(max_length=100)
    done = models.BooleanField(default=False)
