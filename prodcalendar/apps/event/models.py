from django.contrib.auth import get_user_model
from django.db import models

class Event(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='events', null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    in_activity = models.BooleanField(default=True)
