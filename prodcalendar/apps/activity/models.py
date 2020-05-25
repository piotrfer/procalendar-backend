from django.contrib.auth import get_user_model
from django.db import models
import datetime as dt

class Activity(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='activities')
    title = models.CharField(max_length=100)
    description = models.TextField()
    start = models.TimeField()
    end = models.TimeField(default=dt.time(hour=1,minute=30))

    categories = (
        ('WRK', 'work'),
        ('SCH', 'school'),
        ('HOB', 'hobby'),
        ('SOC', 'social'),
        ('NED', 'needs'),
        ('FUN', 'fun'),
        ('REL', 'relax')
    )
        
    days = (
        ('MON','monday'),
        ('TUE','tuesday'),
        ('WED','wednesday'),
        ('THU','thursday'),
        ('FRI','friday'),
        ('SAT','saturday'),
        ('SUN','sunday')
    )
    
    category = models.CharField(max_length=3, choices=categories)
    day = models.CharField(max_length=3, choices=days)

    def __str__(self):
        return self.title