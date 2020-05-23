from django.db import models
from django.contrib.auth.models import AbstractUser
from ..activity.models import Activity

class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    activities = models.ManyToManyField(Activity, verbose_name=("Activity"))
    REQUIRED_FIELDS = ['username', 'first_name']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email
