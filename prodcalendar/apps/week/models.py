from django.db import models
from ..activity.models import Activity

class Week(models.Model):
    activities = models.ForeignKey(Activity, on_delete=models.CASCADE)
