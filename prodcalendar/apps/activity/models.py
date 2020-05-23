from django.db import models

class Activity(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()
    start = models.TimeField()
    
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